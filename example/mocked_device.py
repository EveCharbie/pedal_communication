from pedal_communication.mockers import PedalDeviceMocker


def main():
    mocker = PedalDeviceMocker()

    while True:
        # Restart the mocker indefinitely if it disconnects
        mocker.run()


if __name__ == "__main__":
    main()
