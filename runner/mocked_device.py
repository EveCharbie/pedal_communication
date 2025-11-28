from pedal_communication.mockers import PedalDeviceMocker


def main():
    mocker = PedalDeviceMocker()

    for i in range(3):
        mocker.run()


if __name__ == "__main__":
    main()
