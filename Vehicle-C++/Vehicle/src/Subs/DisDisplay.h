/**
 * @file DisDisplay.h
 * @author Team Sleipnir
 * @brief Contains the Miles traveled subscriber
 * @version 0.1
 * @date 2022-07-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#ifndef MOVING_H
#define MOVING_H

#include "../Miles/MilesPubSubTypes.h"

#include <fastdds/dds/domain/DomainParticipantFactory.hpp>
#include <fastdds/dds/domain/DomainParticipant.hpp>
#include <fastdds/dds/topic/TypeSupport.hpp>
#include <fastdds/dds/subscriber/Subscriber.hpp>
#include <fastdds/dds/subscriber/DataReader.hpp>
#include <fastdds/dds/subscriber/DataReaderListener.hpp>
#include <fastdds/dds/subscriber/qos/DataReaderQos.hpp>
#include <fastdds/dds/subscriber/SampleInfo.hpp>

using namespace eprosima::fastdds::dds;

/**
    * @brief Distance Display Subscriber that will subscribe to the 
    * MilesTravled topic.
    * 
    */
class DDSubscriber {
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
    DDSubscriber()
        : participant_(nullptr)
        , subscriber_(nullptr)
        , topic_(nullptr)
        , reader_(nullptr)
        , type_(new MilesPubSubType())
    {
    }

    virtual ~DDSubscriber()
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
     * @brief Checks to see if miles traveled is larger than 0
     * 
     */
    void run()
    {
        double total = 0;
        while (1) {
            if (listener_.miles_.milesTraveled() > 0) {
                total = total + listener_.miles_.milesTraveled();
                std::cout << "Odometer: " << std::fixed << std::setprecision(1) << total << std::endl;
                std::this_thread::sleep_for(std::chrono::milliseconds(250));
            } else {
                std::cout << "Odometer: " << std::fixed << std::setprecision(1) << total << std::endl;
                std::this_thread::sleep_for(std::chrono::milliseconds(250));
            }
        }
    }
};

#endif