import argparse
import pefile
import sys
from pathlib import Path

banner = """
       ▄▄▄ . ▐ ▄  ▌ ▐·       ▄· ▄▌▄▄▄ .▄▄▄      Author: Ved Prakash Gupta (v3dSec)
       ▀▄.▀·•█▌▐█▪█·█▌▪     ▐█▪██▌▀▄.▀·▀▄ █·    Github: https://github.com/v3dSec
       ▐▀▀▪▄▐█▐▐▌▐█▐█• ▄█▀▄ ▐█▌▐█▪▐▀▀▪▄▐▀▀▄     Twitter: https://x.com/v3dSec
       ▐█▄▄▌██▐█▌ ███ ▐█▌.▐▌ ▐█▀·.▐█▄▄▌▐█•█▌
        ▀▀▀ ▀▀ █▪. ▀   ▀█▄▀▪  ▀ •  ▀▀▀ .▀  ▀
"""


def generate_export_directives(dll_path, proxy_dll_name, output_file_path):
    """
    Parses the export table of the specified DLL and generates
    linker export directives suitable for creating a proxy DLL.
    """
    try:
        pe = pefile.PE(dll_path)
    except OSError as error:
        print(f"ERROR: Unable to open the PE file: {error}")
        sys.exit(1)

    dll_basename = proxy_dll_name if proxy_dll_name else Path(dll_path).stem

    export_directives = []
    for symbol in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        if symbol.name:
            func_name = symbol.name.decode()
            # Generate export directive for named exports.
            directive = f'#pragma comment(linker, "/export:{func_name}={dll_basename}.{func_name},@{symbol.ordinal}")'
        else:
            # Generate export directive for unnamed exports.
            directive = f'#pragma comment(linker, "/export:NONAME={dll_basename}.#{symbol.ordinal},@{symbol.ordinal},NONAME")'
        export_directives.append(directive)

    if output_file_path:
        with open(output_file_path, "w") as output_file:
            output_file.write("\n".join(export_directives) + "\n")
        print(f"\nExport directives have been written to: {output_file_path}")
    else:
        for directive in export_directives:
            print(directive)


def main():

    parser = argparse.ArgumentParser(
        description="Generate export directives for creating a proxy DLL for (DLL sideloading or DLL hijacking)."
    )

    parser.add_argument(
        "-d",
        "--dll-path",
        type=str,
        required=True,
        help="The path to the DLL file whose exports will be parsed.",
    )

    parser.add_argument(
        "-p",
        "--proxy-dll",
        type=str,
        default=None,
        help="The name of the DLL to which function calls will be proxied.",
    )

    parser.add_argument(
        "-o",
        "--output-file",
        type=str,
        default=None,
        help="The output file to save the generated export directives.",
    )

    if len(sys.argv) == 1:
        print(banner)
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    generate_export_directives(args.dll_path, args.proxy_dll, args.output_file)


if __name__ == "__main__":
    main()
