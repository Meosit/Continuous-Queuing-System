from arguments import parse_arguments
from channel import Channel
from generator import Generator

mu1 = 5
mu2 = 110.379
lmbd = 9.5
normalizing_factor = 0
accuracy = 100


def main():
    arguments = parse_arguments()
    normailze_inputs(arguments)

    first_chanel = Channel(mu1)
    second_chanel = Channel(mu2)
    generator = Generator(lmbd)
    ticks_number = 100000 * accuracy
    declined_claims = 0
    generated_claims = 0
    processed_claims = 0
    for i in range(0, ticks_number):
        if generator.is_generated():
            generator.start_generate()
            generated_claims += 1
            if first_chanel.is_processed():
                first_chanel.add()
                processed_claims += 1
            elif second_chanel.is_processed():
                second_chanel.add()
                processed_claims += 1
            else:
                declined_claims += 1
        first_chanel.tick()
        second_chanel.tick()
        generator.tick()

    print('Occupancy of first chanel: ', first_chanel.work_time / ticks_number)
    print('Occupancy of second chanel: ', second_chanel.work_time / ticks_number)
    print('Decline probability: ', declined_claims / generated_claims)
    print('Relative system capacity: ', processed_claims / generated_claims)
    print('Absolute system capacity: ', processed_claims
          * normalizing_factor / ticks_number)


def normailze_inputs(arguments):
    global mu1
    global mu2
    global lmbd
    global normalizing_factor
    mu1 = arguments.mu1
    mu2 = arguments.mu2
    lmbd = arguments.lmbd
    normalizing_factor = max(mu1, mu2, lmbd) * accuracy
    mu1 = mu1 / normalizing_factor
    mu2 = mu2 / normalizing_factor
    lmbd = lmbd / normalizing_factor


if __name__ == "__main__":
    main()
