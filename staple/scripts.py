#!/usr/bin/env python

def main():
    from optparse import OptionParser
    usage = "usage: %prog publish [--output=output_dir] template_dir"
    usage += "\n      %prog generate output_dir structure_file"
    parser = OptionParser(usage=usage)
    parser.add_option('-o', '--output', dest='output_dir')
    
    (options, args) = parser.parse_args()
    
    if args[0] == 'publish':
        if len(args) < 2:
            parser.error('must provide a template directory')
        
        from publisher import Publisher
        
        if options.output_dir:
            runner = Publisher(template_dir=args[1], output_dir=options.output_dir)
            runner()
        else:
            runner = Publisher(template_dir=args[1])
            runner()
    
    elif args[0] == 'generate':
        if len(args) < 3:
            parser.error('must provide an output directory and a configuration file')
        
        from generator import Generator
        
        runner = Generator(output_dir=args[1], config_file=args[2])
        runner()
    
    else:
        parser.error('invalid command')
    
