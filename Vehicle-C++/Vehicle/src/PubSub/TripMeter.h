/**
 * @file TripMeter.h
 * @author Team Sleipnir
 * @brief Contains all the pub/subs within the TripMeter class
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#ifndef TRIPMETER_H
#define TRIPMETER_H

#include "../Calculations.cpp"
#include "../TripMeter/TripPubSubTypes.h"
#include "../MPG/MpGPubSubTypes.cxx"
#include "../MPG/MpG.cxx"
#include "../Miles/Miles.cxx"
#include "../Miles/MilesPubSubTypes.cxx"

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

/**
 * @brief TripMeter Class that will hold all the Pub/Sub for the TripMeter publisher
 * and stores all the private data variables that are shared between the Pub/Subs
 * 
 */
class TripMeter {
private:
    double MT;
    double MPG;
    double time;
    unsigned long MTindex, MPGindex, TMindex;

public:
    TripMeter()
        : MT(0)
        , MPG(0)
        , time(0)
        , MTindex(0)
        , MPGindex(0)
        , TMindex(0)
    {
    }

    ~TripMeter()
    {
    }

    /**
    * @brief Miles Traveled Subscriber that will subscribe to the Miles Travled topic and store the data 
    * locally in the upper class.
    * 
    */
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
                    std::cout << "MTPublisher matched." << std::endl;
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

        /**
        * @brief Will take the Miles Traveled data and save it to the upper class MT variable
        * and increment the MTindex up by 1.
        * 
        * @param data TripMeter Object Variable
        */
        void run(TripMeter* data)
        {
            unsigned long old = 0;
            while (1) {
                if (listener_.samples_ != old) {
                    if (data->MTindex == data->TMindex) {
                        data->MT = listener_.miles_.milesTraveled();
                        old = listener_.samples_;
                        data->MTindex = data->MTindex + 1;
                    }
                }
            }
        }
    };

    /**
    * @brief MPG Subscriber that will subscribe to the MPG topic and store the data 
    * locally in the upper class.
    * 
    */
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
                    std::cout << "MPGPublisher matched." << std::endl;
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

        /**
         * @brief Will take the MPG data and save it to the upper class MPG variable
         * and increment the MPGindex up by 1.
         * 
         * @param data TripMeter Object Variable
         */
        void run(TripMeter* data)
        {
            unsigned long old = 0;
            while (1) {
                if (listener_.samples_ != old) {
                    if (data->TMindex == data->MPGindex) {
                        data->MPG = listener_.mpg_.mpg();
                        old = listener_.samples_;
                        data->MPGindex = data->MPGindex + 1;
                    }
                }
            }
        }
    };

    /**
    * @brief Trip Meter publisher that will post the Trip Meter data to the 
    * TripMeter topic.
    * 
    */
    class TMPublisher {
    private:
        Trip trip_;

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
        TMPublisher()
            : participant_(nullptr)
            , publisher_(nullptr)
            , topic_(nullptr)
            , writer_(nullptr)
            , type_(new TripPubSubType())
        {
        }

        virtual ~TMPublisher()
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
            trip_.miles(0);
            trip_.MPG(0);
            trip_.speed(0);
            trip_.time(0);

            DomainParticipantQos participantQos;
            participantQos.name("Participant_publisher");
            participant_ = DomainParticipantFactory::get_instance()->create_participant(0, participantQos);

            if (participant_ == nullptr) {
                return false;
            }

            // Register the Type
            type_.register_type(participant_);

            // Create the publications Topic
            topic_ = participant_->create_topic("TripMeter", "Trip", TOPIC_QOS_DEFAULT);

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
        * @brief Publishes Trip Meter data onto the topic if MTindex & MPGindex are 
        * greater than MPGindex.
        * 
        * @param calc_ TM Object variable from Calculations.h
        * @param data TripMeter Object variable
        * @return true 
        * @return false 
        */
        bool publish(TM* calc_, TripMeter* data)
        {
            if (data->TMindex < data->MPGindex && data->TMindex < data->MTindex) {
                std::tie(trip_.miles(), trip_.speed(), trip_.time(), trip_.MPG()) = calc_->GetTripData();
                writer_->write(&trip_);
                data->TMindex = data->TMindex + 1;
                return true;
            }
            trip_.time() = trip_.time() + data->time;
            writer_->write(&trip_);
            return false;
        }

        /**
        * @brief Will check to see if publish returns true or false, it will update the
        * TripMeter topic data in Calculation every 0.25 secs, and will wait 0.25 secs.
        * 
        * @param calc_ TM object varaible from Calculations.h
        * @param data Trip Meter Object varaible
        */
        void run(TM* calc_, TripMeter* data)
        {
            while (1) {
                if (publish(calc_, data)) {
                    std::cout << "Miles: " << trip_.miles() << std::endl;
                    std::cout << "Avg Speed: " << trip_.speed() << std::endl;
                    std::cout << "Time: " << trip_.time() / 60 << std::endl;
                    std::cout << "Avg MPG: " << trip_.MPG() << std::endl;
                    std::cout << std::endl;
                } else {
                    std::cout << "0Miles: " << trip_.miles() << std::endl;
                    std::cout << "0Avg Speed: " << trip_.speed() << std::endl;
                    std::cout << "0Time: " << trip_.time() / 60 << std::endl;
                    std::cout << "0Avg MPG: " << trip_.MPG() << std::endl;
                    std::cout << std::endl;
                }
                calc_->updateTrip(data->MT, data->MPG, data->time);
                std::this_thread::sleep_for(std::chrono::milliseconds(250));
            }
        }

        /**
        * @brief Gets accurate time info and saves it to data.time for future use
        * 
        * @param data trip meter object
        */
        void time(TripMeter* data)
        {
            while (1) {
                auto start = std::chrono::high_resolution_clock::now();
                std::this_thread::sleep_for(std::chrono::milliseconds(250));
                auto stop = std::chrono::high_resolution_clock::now();
                std::chrono::duration<double> diff = stop - start;
                data->time = diff.count();
            }
        }
    };
};

#endif