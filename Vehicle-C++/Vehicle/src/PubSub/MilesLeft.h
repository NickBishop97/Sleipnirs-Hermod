#ifndef MILESLEFT_H
#define MILESLEFT_H

#include "../Calculations.cpp"
#include "../MilesLeft/MilesToRefuelPubSubTypes.h"
#include "../MPG/MpGPubSubTypes.cxx"
#include "../MPG/MpG.cxx"
#include "../Fuel/FuelPubSubTypes.cxx"
#include "../Fuel/Fuel.cxx"

#include <fastdds/dds/domain/DomainParticipantFactory.hpp>
#include <fastdds/dds/domain/DomainParticipant.hpp>
#include <fastdds/dds/topic/TypeSupport.hpp>
#include <fastdds/dds/publisher/Publisher.hpp>
#include <fastdds/dds/publisher/DataWriter.hpp>
#include <fastdds/dds/publisher/DataWriterListener.hpp>
#include <fastdds/dds/subscriber/Subscriber.hpp>
#include <fastdds/dds/subscriber/DataReader.hpp>
#include <fastdds/dds/subscriber/DataReaderListener.hpp>
#include <fastdds/dds/subscriber/qos/DataReaderQos.hpp>
#include <fastdds/dds/subscriber/SampleInfo.hpp>

using namespace eprosima::fastdds::dds;

class MilesLeft {
private:
    double FR;
    double MPG;
    unsigned long MPGindex;
    unsigned long FRindex;
    unsigned long MLindex;

public:
    MilesLeft()
        : FR(0.0)
        , MPG(0.0)
        , MPGindex(0)
        , FRindex(0)
        , MLindex(0)
    {
    }

    ~MilesLeft()
    {
    }

    class MPGSubscriber {
    private:
        DomainParticipant* participant_;

        Subscriber* subscriber_;

        DataReader* reader_;

        Topic* topic_;

        TypeSupport type_;

        class SubListener : public DataReaderListener {
        public:
            SubListener()
                : samples_(0)
            {
            }

            ~SubListener() override
            {
            }

            void on_subscription_matched(
                DataReader*,
                const SubscriptionMatchedStatus& info) override
            {
                if (info.current_count_change == 1) {
                    std::cout << "Publisher matched." << std::endl;
                } else if (info.current_count_change == -1) {
                    std::cout << "Publisher unmatched." << std::endl;
                } else {
                    std::cout << info.current_count_change
                              << " is not a valid value for PublisherMatchedStatus current count change" << std::endl;
                }
            }

            void on_data_available(
                DataReader* reader) override
            {
                SampleInfo info;
                if (reader->take_next_sample(&mpg_, &info) == ReturnCode_t::RETCODE_OK) {
                    if (info.valid_data) {
                        samples_++;
                    }
                }
            }

            MpG mpg_;

            std::atomic_int samples_;

        } listener_;

    public:
        MPGSubscriber()
            : participant_(nullptr)
            , subscriber_(nullptr)
            , topic_(nullptr)
            , reader_(nullptr)
            , type_(new MpGPubSubType())
        {
        }

        virtual ~MPGSubscriber()
        {
            if (reader_ != nullptr) {
                subscriber_->delete_datareader(reader_);
            }
            if (topic_ != nullptr) {
                participant_->delete_topic(topic_);
            }
            if (subscriber_ != nullptr) {
                participant_->delete_subscriber(subscriber_);
            }
            DomainParticipantFactory::get_instance()->delete_participant(participant_);
        }

        //!Initialize the subscriber
        bool init()
        {
            DomainParticipantQos participantQos;
            participantQos.name("Participant_subscriber");
            participant_ = DomainParticipantFactory::get_instance()->create_participant(0, participantQos);

            if (participant_ == nullptr) {
                return false;
            }

            // Register the Type
            type_.register_type(participant_);

            // Create the subscriptions Topic
            topic_ = participant_->create_topic("MPG", "MpG", TOPIC_QOS_DEFAULT);

            if (topic_ == nullptr) {
                return false;
            }

            // Create the Subscriber
            subscriber_ = participant_->create_subscriber(SUBSCRIBER_QOS_DEFAULT, nullptr);

            if (subscriber_ == nullptr) {
                return false;
            }

            // Create the DataReader
            reader_ = subscriber_->create_datareader(topic_, DATAREADER_QOS_DEFAULT, &listener_);

            if (reader_ == nullptr) {
                return false;
            }

            return true;
        }

        void run(MilesLeft* data)
        {
            unsigned long old = 0;
            while (1) {
                if (listener_.samples_ != old) {
                    if (data->MLindex == data->MPGindex) {
                        data->MPG = listener_.mpg_.mpg();
                        old = listener_.samples_;
                        data->MPGindex = data->MPGindex + 1;
                    }
                }
            }
        }
    };

    class FRSubscriber {
    private:
        DomainParticipant* participant_;

        Subscriber* subscriber_;

        DataReader* reader_;

        Topic* topic_;

        TypeSupport type_;

        class SubListener : public DataReaderListener {
        public:
            SubListener()
                : samples_(0)
            {
            }

            ~SubListener() override
            {
            }

            void on_subscription_matched(
                DataReader*,
                const SubscriptionMatchedStatus& info) override
            {
                if (info.current_count_change == 1) {
                    std::cout << "Publisher matched." << std::endl;
                } else if (info.current_count_change == -1) {
                    std::cout << "Publisher unmatched." << std::endl;
                } else {
                    std::cout << info.current_count_change
                              << " is not a valid value for PublisherMatchedStatus current count change" << std::endl;
                }
            }

            void on_data_available(
                DataReader* reader) override
            {
                SampleInfo info;
                if (reader->take_next_sample(&fuel_, &info) == ReturnCode_t::RETCODE_OK) {
                    if (info.valid_data) {
                        samples_++;
                    }
                }
            }

            Fuel fuel_;

            std::atomic_int samples_;

        } listener_;

    public:
        FRSubscriber()
            : participant_(nullptr)
            , subscriber_(nullptr)
            , topic_(nullptr)
            , reader_(nullptr)
            , type_(new FuelPubSubType())
        {
        }

        virtual ~FRSubscriber()
        {
            if (reader_ != nullptr) {
                subscriber_->delete_datareader(reader_);
            }
            if (topic_ != nullptr) {
                participant_->delete_topic(topic_);
            }
            if (subscriber_ != nullptr) {
                participant_->delete_subscriber(subscriber_);
            }
            DomainParticipantFactory::get_instance()->delete_participant(participant_);
        }

        //!Initialize the subscriber
        bool init()
        {
            DomainParticipantQos participantQos;
            participantQos.name("Participant_subscriber");
            participant_ = DomainParticipantFactory::get_instance()->create_participant(0, participantQos);

            if (participant_ == nullptr) {
                return false;
            }

            // Register the Type
            type_.register_type(participant_);

            // Create the subscriptions Topic
            topic_ = participant_->create_topic("FuelRemain", "Fuel", TOPIC_QOS_DEFAULT);

            if (topic_ == nullptr) {
                return false;
            }

            // Create the Subscriber
            subscriber_ = participant_->create_subscriber(SUBSCRIBER_QOS_DEFAULT, nullptr);

            if (subscriber_ == nullptr) {
                return false;
            }

            // Create the DataReader
            reader_ = subscriber_->create_datareader(topic_, DATAREADER_QOS_DEFAULT, &listener_);

            if (reader_ == nullptr) {
                return false;
            }

            return true;
        }

        void run(MilesLeft* data)
        {
            unsigned long old = 0;
            while (1) {
                if (listener_.samples_ != old) {
                    if (data->FRindex == data->MLindex) {
                        data->FR = listener_.fuel_.litersRemaining();
                        old = listener_.samples_;
                        data->FRindex = data->FRindex + 1;
                    }
                }
            }
        }
    };

    class MLPublisher {
    private:
        MilesToRefuel milesleft_;

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
        MLPublisher()
            : participant_(nullptr)
            , publisher_(nullptr)
            , topic_(nullptr)
            , writer_(nullptr)
            , type_(new MilesToRefuelPubSubType())
        {
        }

        virtual ~MLPublisher()
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

        /**
                 * @brief Initializes the DDS Publisher with correct topic and initial starting data
                 * 
                 * @return true if system started without a problme
                 * @return false if system didn't start correctly
                 */
        bool init()
        {
            milesleft_.milesToRefuel(0);

            DomainParticipantQos participantQos;
            participantQos.name("Participant_publisher");
            participant_ = DomainParticipantFactory::get_instance()->create_participant(0, participantQos);

            if (participant_ == nullptr) {
                return false;
            }

            // Register the Type
            type_.register_type(participant_);

            // Create the publications Topic
            topic_ = participant_->create_topic("MilesLeft", "MilesToRefuel", TOPIC_QOS_DEFAULT);

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
                 * @brief Publishes MilesToRefuel data onto the topic
                 * 
                 * @param calc_ Houses all the calculation functions that are required to calc the miles left
                 * @param data  Houses data from the two local subscribers
                 * @return true 
                 * @return false 
                 */
        bool publish(ML* calc_, MilesLeft* data)
        {
            if (data->MLindex < data->MPGindex && data->MLindex < data->FRindex) {
                milesleft_.milesToRefuel(calc_->get_MilesLeft(data->MPG, data->FR));
                data->MLindex = data->MLindex + 1;
                writer_->write(&milesleft_);
                return true;
            }
            return false;
        }

        /**
                 * @brief Will check to see if publish returns true or false and wait 0.25 secs
                 * 
                 * @param calc_
                 * @param data 
                 */
        void run(ML* calc_, MilesLeft* data)
        {
            while (1) {
                //std::cout << data->FR << " " << data->MPG << std::endl;
                if (publish(calc_, data)) {
                    if (milesleft_.milesToRefuel() == -1) {
                        std::cout << "Miles Left: 0" << std::endl;
                    } else {
                        std::cout << std::fixed << std::setprecision(2) << "Miles Left: " << milesleft_.milesToRefuel() << std::endl;
                    }
                } else {
                    std::cout << "Miles Left: 0" << std::endl;
                }
                std::this_thread::sleep_for(std::chrono::milliseconds(250));
            }
        }
    };
};
#endif