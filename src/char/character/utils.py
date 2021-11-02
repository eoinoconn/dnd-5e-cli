from textwrap import dedent

from .create import execute as character_create_execute

def configure_parser_create(sub_parser) -> None:
    help = ""
    descr = (help + "") #TODO: Fill this in

    example = dedent("""
    Examples:
        conda create -n myenv sqlite
    """)
    parser = sub_parser.add_parser(
        'create',
        description=descr,
        help=help,
        epilog=example,
    )

    parser.set_defaults(func=character_create_execute)
