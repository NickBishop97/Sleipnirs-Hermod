#ifndef MILESTRAVELED_H
#define MILESTRAVELED_H

#include "../Calculations.cpp"
#include "../Miles/MilesPubSubTypes.h"
#include "../Miles/Miles.h"
#include "../Moving/MovePubSubTypes.cxx"
#include "../Moving/Move.cxx"

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
 * @brief Miles Publisher that will publisher the Miles Traveled data onto the MilesTraveled topic
 * 
 */
class MilesPublisher {
private:
    Miles miles_;

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
    MilesPublisher()
        : participant_(nullptr)
        , publisher_(nullptr)
        , topic_(nullptr)
        , writer_(nullptr)
        , type_(new MilesPubSubType())
    {
    }

    virtual ~MilesPublisher()
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
        miles_.index(0);
        miles_.milesTraveled(0);

        DomainParticipantQos participantQos;
        participantQos.name("Participant_publisher");
        participant_ = DomainParticipantFactory::get_instance()->create_participant(0, participantQos);

        if (participant_ == nullptr) {
            return false;
        }

        // Register the Type
        type_.register_type(participant_);

        // Create the publications Topic
        topic_ = participant_->create_topic("MilesTravled", "Miles", TOPIC_QOS_DEFAULT);

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
     * @brief Publishes Miles Traveled data onto the topic
     * 
     * @param calc_ 
     * @return true if Moving sub recieved a 1/0
     * @return false if Moving sub recieved a non 1/0 
     */
    bool publish(MilesTraveled* calc_)
    {
        double traveled;
        traveled = ((1.2) * rand() / RAND_MAX + 0.05);
        if (calc_->get_index() == 1) {
            miles_.milesTraveled(traveled);
            writer_->write(&miles_);
            return true;
        } else if (calc_->get_index() == 0) {
            miles_.milesTraveled(0);
            writer_->write(&miles_);
            return true;
        }
        miles_.index(calc_->get_index());
        return false;
    }

    /**
     * @brief Will check to see if publish returns true or false and wait 0.25 secs
     * 
     * @param calc_ 
     */
    void run(MilesTraveled* calc_)
    {
        while (1) {
            if (publish(calc_)) {
                std::cout << "Miles Traveled: " << miles_.milesTraveled()
                          << std::endl;
            } else {
                std::cout << "Moving Sub recieved a non 0/1 value: " << miles_.index()
                          << std::endl;
            }
            std::this_thread::sleep_for(std::chrono::milliseconds(250));
        }
    }
};

/**
 * @brief Will Subscribe to the Moving topic and grab the ismoving value 
 * 
 */
class MoveSubscriber {
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
            if (reader->take_next_sample(&move_, &info) == ReturnCode_t::RETCODE_OK) {
                if (info.valid_data) {
                    if (move_.ismoving() != 0) {
                        samples_++;
                    }
                }
            }
        }

        Move move_;

        std::atomic_int samples_;

    } listener_;

public:
    MoveSubscriber()
        : participant_(nullptr)
        , subscriber_(nullptr)
        , topic_(nullptr)
        , reader_(nullptr)
        , type_(new MovePubSubType())
    {
    }

    virtual ~MoveSubscriber()
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
        topic_ = participant_->create_topic("Moving", "Move", TOPIC_QOS_DEFAULT);

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
     * @brief Will set the index to calc_ class to 1/0 if the car is moving or not every 0.25sec
     * 
     * @param calc_ 
     */
    void run(MilesTraveled* calc_)
    {
        unsigned long old = 0;
        while (1) {
            if (listener_.samples_ == old) {
                calc_->set_index(0);
            } else {
                calc_->set_index(1);
            }
            old = listener_.samples_;
            std::this_thread::sleep_for(std::chrono::milliseconds(251));
        }
    }
};

#endif