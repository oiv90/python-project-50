from gendiff import cli, generate_difference


def main():
    args = cli.parse_args()
    return generate_difference(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()