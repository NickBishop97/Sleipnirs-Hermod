#include "FuelPubSubTypes.h"

#include <fastdds/dds/domain/DomainParticipantFactory.hpp>
#include <fastdds/dds/domain/DomainParticipant.hpp>
#include <fastdds/dds/topic/TypeSupport.hpp>
#include <fastdds/dds/publisher/Publisher.hpp>
#include <fastdds/dds/publisher/DataWriter.hpp>
#include <fastdds/dds/publisher/DataWriterListener.hpp>

using namespace eprosima::fastdds::dds;

class FuelPublisher
{
private:

    Fuel fuel_;

    DomainParticipant* participant_;

    Publisher* publisher_;

    Topic* topic_;

    DataWriter* writer_;

    TypeSupport type_;

    class PubListener : public DataWriterListener
    {
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
            if (info.current_count_change == 1)
            {
                matched_ = info.total_count;
                std::cout << "Subscriber matched. " << matched_ << std::endl;
            }
            else if (info.current_count_change == -1)
            {
                matched_ = info.current_count;
                std::cout << "Subscriber unmatched. " << matched_ << std::endl;
            }
            else
            {
                std::cout << info.current_count_change
                        << " is not a valid value for SubscriberMatchedStatus current count change." << std::endl;
            }
        }

        std::atomic_int matched_;

    } listener_;

public:

    FuelPublisher()
        : participant_(nullptr)
        , publisher_(nullptr)
        , topic_(nullptr)
        , writer_(nullptr)
        , type_(new FuelPubSubType())
    {
    }

    virtual ~FuelPublisher()
    {
        if (writer_ != nullptr)
        {
            publisher_->delete_datawriter(writer_);
        }
        if (publisher_ != nullptr)
        {
            participant_->delete_publisher(publisher_);
        }
        if (topic_ != nullptr)
        {
            participant_->delete_topic(topic_);
        }
        DomainParticipantFactory::get_instance()->delete_participant(participant_);
    }

    //!Initialize the publisher
    bool init()
    {
        fuel_.index(10);
        fuel_.message("Litters Left: ");

        DomainParticipantQos participantQos;
        participantQos.name("Participant_publisher");
        participant_ = DomainParticipantFactory::get_instance()->create_participant(0, participantQos);

        if (participant_ == nullptr)
        {
            return false;
        }

        // Register the Type
        type_.register_type(participant_);

        // Create the publications Topic
        topic_ = participant_->create_topic("FuelRemaining", "Fuel", TOPIC_QOS_DEFAULT);

        if (topic_ == nullptr)
        {
            return false;
        }

        // Create the Publisher
        publisher_ = participant_->create_publisher(PUBLISHER_QOS_DEFAULT, nullptr);

        if (publisher_ == nullptr)
        {
            return false;
        }

        // Create the DataWriter
        writer_ = publisher_->create_datawriter(topic_, DATAWRITER_QOS_DEFAULT, &listener_);

        if (writer_ == nullptr)
        {
            return false;
        }
        return true;
    }

    //!Send a publication
    bool publish()
    {
        double loss;
        if (listener_.matched_ > 0)
        {
            loss = ((0.1)*rand()/RAND_MAX + 0.01);
            if((fuel_.index() - loss) < 0)
            {
                fuel_.index(0);
                writer_->write(&fuel_);
                return true;
            }
            else
            {
                fuel_.index(fuel_.index() - loss);
                writer_->write(&fuel_);
                return true;
            }
        }
        return false;
    }

    //!Run the Publisher
    void run()
    {
        while (1)
        {
            if (publish())
            {
                std::cout << fuel_.message() << fuel_.index()
                            <<  std::endl;
            }
            std::this_thread::sleep_for(std::chrono::milliseconds(250));
        }
    }
    //!Checks to see if tank is empty
    // This will check to see if the tank is empty, if it is empty
    // then it will fill the tank randomly from 1 to 10 Litters
    void check()
    {
        double gain;
        while(1)
        {
            if(fuel_.index() == 0)
            {
                gain = (rand()%10)+1;
                std::this_thread::sleep_for(std::chrono::milliseconds(3000));
                fuel_.index() = gain;
                std::cout << "Tank filled with " << fuel_.index() << "L" << std::endl;
            }
            std::this_thread::sleep_for(std::chrono::milliseconds(500));
        }
    }
};

int main(
        int argc,
        char** argv)
{
    std::cout << "Publishing Fuel Status." << std::endl;
    int samples = 100;
    srand(time(0));

    FuelPublisher* mypub = new FuelPublisher();
    if(mypub->init())
    {
        //starts up two threads send fuel info and check tank
        std::thread sendfuel (&FuelPublisher::run, mypub);
        std::thread checktank (&FuelPublisher::check, mypub);
        sendfuel.join();
        checktank.join();
    }

    delete mypub;
    return 0;
}