
# argparse + tornado = argserve

Serve your command line python scripts via the web!
This library will serve your command line script via a web interface.
The only thing you have to do is create a wrapper script, call
the `serve` method!


    from argserve import serve
    from my_cool_cli import parser, main
    
    serve(parser, main)

Where parser is an `argparse.ArgumentParser` and `main` a function that
takes the parsed arguments.

What argserve does, is render a nice form for the commandline arguments
and when the form is submitted, it feeds the given parameters to
the main function.
