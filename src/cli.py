from argparse import ArgumentParser


def cli_args():
    args = ArgumentParser("Params for processing .FASTA files")
    args.add_argument(
        "-m",
        "--match",
        required=False,
        default=2,
        type=int,
        help="Input the match value. Defaults to 2",
    )
    args.add_argument(
        "-M",
        "--missmatch",
        required=False,
        default=-3,
        type=int,
        help="Input the missmatch value. Defaults to -3",
    )
    args.add_argument(
        "-g",
        "--gap",
        required=False,
        default=-4,
        type=int,
        help="Input the gap value. Defaults to -4",
    )
    return args
