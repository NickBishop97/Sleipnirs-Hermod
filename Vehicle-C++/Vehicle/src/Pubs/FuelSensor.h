/**
 * @file FuelSensor.h
 * @author Nick Bishop
 * @brief Contains all the Publishers for The Fuelsensor
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#ifndef FUELSENSOR_H
#define FUELSENSOR_H

#include "../Calculations.cpp"
#include "../Fuel/FuelPubSubTypes.h"

#include <fastdds/dds/domain/DomainParticipantFactory.hpp>
#include <fastdds/dds/domain/DomainParticipant.hpp>
#include <fastdds/dds/topic/TypeSupport.hpp>
#include <fastdds/dds/publisher/Publisher.hpp>
#include <fastdds/dds/publisher/DataWriter.hpp>
#include <fastdds/dds/publisher/DataWriterListener.hpp>

using namespace eprosima::fastdds::dds;

/**
 * @brief Fuel Sensor Class that will hold all of the Pubs and store private local
 * variables for the Pubs.
 * 
 */
class FS {
private:
    unsigned long index;
    unsigned long check;

public:
    FS()
        : index(0)
        , check(1)
    {
    }

    ~FS()
    {
    }

    /**
    * @brief Fuel Remaining Publisher that will publisher the FuelRemaining data onto the 
    * FuelRemain topic.
    * 
    */
    class FuelRemainPublisher {
    private:
        Fuel fuel_;

        DomainParticipant* participant_;

        Publisher* publisher_;

        Topic* topic_;

        DataWriter* writer_;

        TypeSupport type_;

        class PubListener : public DataWriterListener {
        public:
            PubListener()
                : matched_(0)
            {
            }

            ~PubListener() override
            {
            }

            void on_publication_matched(
                DataWriter*,
                const PublicationMatchedStatus& info) override
            {
                if (info.current_count_change == 1) {
                    matched_ = info.total_count;
                    std::cout << "Subscriber matched. " << std::endl;
                } else if (info.current_count_change == -1) {
                    matched_ = info.current_count;
                    std::cout << "Subscriber unmatched. " << std::endl;
                } else {
                    std::cout << info.current_count_change
                              << " is not a valid value for SubscriberMatchedStatus current count change." << std::endl;
                }
            }

            std::atomic_int matched_;

        } listener_;

    public:
        FuelRemainPublisher()
            : participant_(nullptr)
            , publisher_(nullptr)
            , topic_(nullptr)
            , writer_(nullptr)
            , type_(new FuelPubSubType())
        {
        }

        virtual ~FuelRemainPublisher()
        {
            if (writer_ != nullptr) {
                publisher_->delete_datawriter(writer_);
            }
            if (publisher_ != nullptr) {
                participant_->delete_publisher(publisher_);
            }
            if (topic_ != nullptr) {
                participant_->delete_topic(topic_);
            }
            DomainParticipantFactory::get_instance()->delete_participant(participant_);
        }

        //!Initialize the publisher
        bool init()
        {
            fuel_.index(0);
            fuel_.litersRemaining(10);
            fuel_.litersSpent(0);

            DomainParticipantQos participantQos;
            participantQos.name("Participant_publisher");
            participant_ = DomainParticipantFactory::get_instance()->create_participant(0, participantQos);

            if (participant_ == nullptr) {
                return false;
            }

            // Register the Type
            type_.register_type(participant_);

            // Create the publications Topic
            topic_ = participant_->create_topic("FuelRemain", "Fuel", TOPIC_QOS_DEFAULT);

            if (topic_ == nullptr) {
                return false;
            }

            // Create the Publisher
            publisher_ = participant_->create_publisher(PUBLISHER_QOS_DEFAULT, nullptr);

            if (publisher_ == nullptr) {
                return false;
            }

            // Create the DataWriter
            writer_ = publisher_->create_datawriter(topic_, DATAWRITER_QOS_DEFAULT, &listener_);

            if (writer_ == nullptr) {
                return false;
            }
            return true;
        }

        //!Send a publication
        bool publish(FS* data)
        {
            double loss;
            loss = ((0.1) * rand() / RAND_MAX + 0.01);
            if (data->check == 1) {
                writer_->write(&fuel_);
                data->check = 0;
                return true;
            } else if ((fuel_.litersRemaining() - loss) < 0) {
                fuel_.litersRemaining(0);
                writer_->write(&fuel_);
                return true;
            } else {
                fuel_.litersRemaining(fuel_.litersRemaining() - loss);
                writer_->write(&fuel_);
                return true;
            }
            return false;
        }

        /**
         * @brief Publishes data on the topic and sets the fuel remaining
         * 
         * @param calc_ FS Object variable
         * @param data FuelSensor Object Variable from Calculations.h
         */
        void run(FuelSenor* calc_, FS* data)
        {
            while (1) {
                if (publish(data)) {
                    calc_->set_FuelRemaining(fuel_.litersRemaining());
                    std::cout << "Litters Remaining: " << fuel_.litersRemaining()
                              << std::endl;
                    fuel_.index() = fuel_.index() + 1;
                    data->index = fuel_.index();
                }
                std::this_thread::sleep_for(std::chrono::milliseconds(250));
            }
        }
        /**
         * @brief Checks to see if tank is empty, if it is then it will fill the 
         * tank randomly from 1 to 10 Litters
         * 
         * @param calc_ FS Object variable
         * @param data FuelSensor Object Variable from Calculations.h
         */
        void check(FuelSenor* calc_, FS* data)
        {
            double gain;
            while (1) {
                if (fuel_.litersRemaining() == 0) {
                    gain = (rand() % 10) + 1;
                    std::this_thread::sleep_for(std::chrono::milliseconds(3000));
                    fuel_.litersRemaining() = gain;
                    calc_->set_FuelRemaining(gain);
                    data->check = 1;
                    std::cout << "Tank filled with " << fuel_.litersRemaining() << "L" << std::endl;
                }
                std::this_thread::sleep_for(std::chrono::milliseconds(500));
            }
        }
    };

    /**
    * @brief Fuel Spent Publisher that will publisher the FuelSpent data onto the FuelSpent topic
    * 
    */
    class FuelSpentPublisher {
    private:
        Fuel fuel_;

        DomainParticipant* participant_;

        Publisher* publisher_;

        Topic* topic_;

        DataWriter* writer_;

        TypeSupport type_;

        class PubListener : public DataWriterListener {
        public:
            PubListener()
                : matched_(0)
            {
            }

            ~PubListener() override
            {
            }

            void on_publication_matched(
                DataWriter*,
                const PublicationMatchedStatus& info) override
            {
                if (info.current_count_change == 1) {
                    matched_ = info.total_count;
                    std::cout << "Subscriber matched. " << matched_ << std::endl;
                } else if (info.current_count_change == -1) {
                    matched_ = info.current_count;
                    std::cout << "Subscriber unmatched. " << matched_ << std::endl;
                } else {
                    std::cout << info.current_count_change
                              << " is not a valid value for SubscriberMatchedStatus current count change." << std::endl;
                }
            }

            std::atomic_int matched_;

        } listener_;

    public:
        FuelSpentPublisher()
            : participant_(nullptr)
            , publisher_(nullptr)
            , topic_(nullptr)
            , writer_(nullptr)
            , type_(new FuelPubSubType())
        {
        }

        virtual ~FuelSpentPublisher()
        {
            if (writer_ != nullptr) {
                publisher_->delete_datawriter(writer_);
            }
            if (publisher_ != nullptr) {
                participant_->delete_publisher(publisher_);
            }
            if (topic_ != nullptr) {
                participant_->delete_topic(topic_);
            }
            DomainParticipantFactory::get_instance()->delete_participant(participant_);
        }

        //!Initialize the publisher
        bool init()
        {
            fuel_.index(0);
            fuel_.litersSpent(0);

            DomainParticipantQos participantQos;
            participantQos.name("Participant_publisher");
            participant_ = DomainParticipantFactory::get_instance()->create_participant(0, participantQos);

            if (participant_ == nullptr) {
                return false;
            }

            // Register the Type
            type_.register_type(participant_);

            // Create the publications Topic
            topic_ = participant_->create_topic("FuelSpent", "Fuel", TOPIC_QOS_DEFAULT);

            if (topic_ == nullptr) {
                return false;
            }

            // Create the Publisher
            publisher_ = participant_->create_publisher(PUBLISHER_QOS_DEFAULT, nullptr);

            if (publisher_ == nullptr) {
                return false;
            }

            // Create the DataWriter
            writer_ = publisher_->create_datawriter(topic_, DATAWRITER_QOS_DEFAULT, &listener_);

            if (writer_ == nullptr) {
                return false;
            }
            return true;
        }

        /**
         * @brief Publishes data onto FuelSpent topic
         * 
         * @param calc_ FS Object variable
         * @param data FuelSensor Object variable in Calculations.h
         * @return true 
         * @return false 
         */
        bool publish(FuelSenor* calc_, FS* data)
        {
            if (data->index > fuel_.index()) {
                double fuelR, fuelS;
                fuelR = calc_->get_FuelRemaining();
                fuelS = calc_->fuelspent(fuelR);
                if (fuelS == -1) {
                    fuelS = 0;
                }
                fuel_.litersSpent(fuelS);
                writer_->write(&fuel_);
                fuel_.index() = fuel_.index() + 1;
                return true;
            } else {
                return false;
            }
        }

        /**
         * @brief Publishes data to topic and prints Litters spent to terminal
         * 
         * @param calc_ FS Object variable
         * @param data FuelSensor Object variable in Calculations.h
         */
        void run(FuelSenor* calc_, FS* data)
        {
            while (1) {
                if (publish(calc_, data)) {
                    std::cout << "Litters Spent: " << fuel_.litersSpent()
                              << std::endl;
                    std::this_thread::sleep_for(std::chrono::milliseconds(248));
                }
            }
        }
    };
};

#endif