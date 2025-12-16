from argparse import ArgumentParser, Namespace

import converter


def main() -> None:
    arg_parser: ArgumentParser = ArgumentParser(
        description="Convert files to Docx file"
    )

    arg_parser.add_argument(
        "inputs", nargs="+", help="Input any file that can be converted"
    )

    arg_parser.add_argument(
        "-o",
        "--output",
        default=converter.DEFAULT_OUTPUT_DOCX,
        help=f"Output docx file (default={converter.DEFAULT_OUTPUT_DOCX})",
    )

    arg_parser.add_argument(
        "--fontname",
        default=converter.DEFAULT_FONT_NAME,
        help=f"font name (default={converter.DEFAULT_FONT_NAME})",
    )

    arg_parser.add_argument(
        "--fontsize",
        type=float,
        default=converter.DEFAULT_FONT_SIZE,
        help=f"font size (default={converter.DEFAULT_FONT_SIZE})",
    )

    args: Namespace = arg_parser.parse_args()

    converter.code_to_docx(args.inputs, args.output, args.fontname, args.fontsize)


if __name__ == "__main__":
    main()
