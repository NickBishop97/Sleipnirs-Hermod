#ifndef MILESTRAVELED_H
#define MILESTRAVELED_H

#include "../Calculations.cpp"
#include "../MPG/MpGPubSubTypes.h"
#include "../MPG/MpG.h"
#include "../Miles/MilesPubSubTypes.cxx"
#include "../Miles/Miles.cxx"
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

class MilesPerGallon
{
    private:
        double MT = 0.0;
        double FS = 0.0;
        unsigned long MTindex = 0, FSindex = 0, MPGindex = 0;
    public:
        class MTSubscriber {
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
                    if (reader->take_next_sample(&miles_, &info) == ReturnCode_t::RETCODE_OK) {
                        if (info.valid_data) {
                            samples_++;
                        }
                    }
                }

                Miles miles_;

                std::atomic_int samples_;

            } listener_;

        public:
            MTSubscriber()
                : participant_(nullptr)
                , subscriber_(nullptr)
                , topic_(nullptr)
                , reader_(nullptr)
                , type_(new MilesPubSubType())
            {
            }

            virtual ~MTSubscriber()
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
                topic_ = participant_->create_topic("MilesTravled", "Miles", TOPIC_QOS_DEFAULT);

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

            void run(MPG* calc_, MilesPerGallon* data)
            {
                unsigned long count = 0;
                unsigned long old = 0;
                while (1) {
                    if (listener_.samples_ != old) {
                        if (data->MTindex == data->MPGindex) {
                            data->MT = listener_.miles_.milesTraveled();
                            data->MTindex = count;
                            count++;
                            old = listener_.samples_;
                        }
                    }
                    //old = listener_.samples_;
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
                topic_ = participant_->create_topic("FuelSpent", "Fuel", TOPIC_QOS_DEFAULT);

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

            void run(MPG* calc_, MilesPerGallon* data)
            {
                unsigned long count = 0;
                unsigned long old = 0;
                while (1) {
                    if (listener_.samples_ != old) {
                        if (data->FSindex == data->MPGindex) {
                            data->FS = listener_.fuel_.litersSpent();
                            data->FSindex = count;
                            count++;
                            old = listener_.samples_;
                        }
                    }
                    //old = listener_.samples_;
                }
            }
        };

        class MPGPublisher {
        private:
            MpG mpg_;

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
            MPGPublisher()
                : participant_(nullptr)
                , publisher_(nullptr)
                , topic_(nullptr)
                , writer_(nullptr)
                , type_(new MpGPubSubType())
            {
            }

            virtual ~MPGPublisher()
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
                mpg_.mpg(0);

                DomainParticipantQos participantQos;
                participantQos.name("Participant_publisher");
                participant_ = DomainParticipantFactory::get_instance()->create_participant(0, participantQos);

                if (participant_ == nullptr) {
                    return false;
                }

                // Register the Type
                type_.register_type(participant_);

                // Create the publications Topic
                topic_ = participant_->create_topic("MPG", "MpG", TOPIC_QOS_DEFAULT);

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
             * @brief Publishes MPG data onto the topic
             * 
             * @param calc_ 
             * @return true 
             * @return false 
             */
            bool publish(MPG* calc_, MilesPerGallon* data)
            {
                //std::cout << "MPG Index: " << calc_->get_MPGindex() << " MT index: " << calc_->get_MTindex() << " FS index: " << calc_->get_FSindex() << std::endl;
                if ((data->MPGindex < data->MTindex) && (data->MPGindex < data->FSindex)) {
                    mpg_.mpg(calc_->mpg(data->MT, data->FS));
                    writer_->write(&mpg_);
                    data->MPGindex = data->MPGindex + 1;
                    return true;
                } else if (data->MTindex > data->FSindex) {
                    mpg_.mpg(calc_->mpg(0, 0));
                    writer_->write(&mpg_);
                    return true;
                } else if (data->MTindex < data->FSindex) {
                    mpg_.mpg(calc_->mpg(0, 0));
                    writer_->write(&mpg_);
                    return true;
                }
                writer_->write(&mpg_);
                return false;
            }

            /**
             * @brief Will check to see if publish returns true or false and wait 0.25 secs
             * 
             * @param calc_ 
             */
            void run(MPG* calc_, MilesPerGallon* data)
            {
                while (1) {
                    if (publish(calc_, data)) {
                        if (mpg_.mpg() == -1.0) {
                            std::cout << std::fixed << std::setprecision(1) << "MPG: -.-" << std::endl;
                        } else {
                            std::cout << std::fixed << std::setprecision(1) << "MPG: " << mpg_.mpg() << std::endl;
                        }
                    } else {
                        std::cout << "MPG: -.-" << std::endl;
                    }
                    //std::cout << "MPG Index: " << calc_->get_MPGindex() << " MT index: " << calc_->get_MTindex() << " FS index: " << calc_->get_FSindex() << std::endl;
                    std::this_thread::sleep_for(std::chrono::milliseconds(250));
                }
            }
        };
};

#endif