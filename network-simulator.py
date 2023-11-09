import numpy as np
import matplotlib.pyplot as plt
import time
import random

# Constants
NUM_COMPUTERS = 3
SIMULATION_TIME = 100  # Time in seconds
MIN_PACKET_SIZE = 100  # Bytes
MAX_PACKET_SIZE = 1000  # Bytes
PACKET_GENERATION_RATE = 5  # Packets per second per computer
BURSTINESS_PROBABILITY = 0.2
BURST_SIZE = 10
MIN_DELAY = 1  # Milliseconds
MAX_DELAY = 10  # Milliseconds
PACKET_LOSS_PROBABILITY = 0.1

# Data structures to store computer information
computers = [{"packets_received": 0, "total_delay": 0.0} for _ in range(NUM_COMPUTERS)]


def simulate_packet_transmission():
    # Simulate packet transmission for the specified duration of the simulation
    for _ in range(SIMULATION_TIME):
        # Simulate packet generation and transmission for each computer
        for computer_id in range(NUM_COMPUTERS):
            # Randomize packet size
            packet_size = random.randrange(MIN_PACKET_SIZE, MAX_PACKET_SIZE)

            # Randomize packet arrival time
            inter_arrival_time = random.expovariate(PACKET_GENERATION_RATE)
            print(inter_arrival_time)
            time.sleep(inter_arrival_time)

            # Introduce burstiness
            if random.random() < BURSTINESS_PROBABILITY:
                # Generate a burst of packets
                for _ in range(BURST_SIZE):
                    generate_and_transmit_packet(computer_id, packet_size)
            else:
                # Generate a single packet
                generate_and_transmit_packet(computer_id, packet_size)


def generate_and_transmit_packet(computer_id, packet_size):
    # Randomize packet delay
    delay = random.uniform(MIN_DELAY, MAX_DELAY)

    # Introduce packet loss
    if random.random() < PACKET_LOSS_PROBABILITY:
        # Drop the packet
        pass
    else:
        # Transmit the packet
        transmit_packet(computer_id, packet_size, delay)


def transmit_packet(computer_id, packet_size, delay):
    # Simulate packet transmission
    time.sleep(2)

    # Update computer statistics
    computers[computer_id]["packets_received"] += 1
    computers[computer_id]["total_delay"] += delay


def plot_packets_per_computer():
    # Plot the number of packets received by each computer
    computer_ids = range(NUM_COMPUTERS)
    packets_received = [computer["packets_received"] for computer in computers]

    plt.figure(figsize=(10, 5))
    plt.bar(computer_ids, packets_received, tick_label=computer_ids)
    plt.xlabel("Computer ID")
    plt.ylabel("Packets Received")
    plt.title("Number of Packets per Computer")
    plt.show()


def plot_average_packet_delay():
    # Plot the average packet delay for each computer
    computer_ids = range(NUM_COMPUTERS)
    avg_delays = [computer["total_delay"] / computer["packets_received"] if computer["packets_received"] > 0 else 0 for computer in computers]

    plt.figure(figsize=(10, 5))
    plt.plot(computer_ids, avg_delays, marker='o')
    plt.xlabel("Computer ID")
    plt.ylabel("Average Delay (ms)")
    plt.title("Average Packet Delay per Computer")
    plt.grid(True)
    plt.show()


def main():
    # Simulate packet transmission
    print("Call packet_transnission function")
    simulate_packet_transmission()

    # Plot the graphs
    plot_packets_per_computer()
    plot_average_packet_delay()


if __name__ == "__main__":
    print("Running script!")
    main()
    print(computers)
