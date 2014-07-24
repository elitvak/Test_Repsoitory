#!perl

use strict;
use warnings;

use CGI::Carp qw(fatalsToBrowser);
use feature qw(switch);

use Net::FTP;
use Net::FTP::File;
use List::MoreUtils 'any';

use Data::Dumper;

# Load the common functions
do "C:/Program Files (x86)/Apache Software Foundation/Apache2.2/htdocs/Tools/Adminconfig.cgi";

my $ftp = Net::FTP->new("141.0.173.18", Debug => 0) or die "Cannot connect to some.host.name: $@";
$ftp->login("test",'somepass') or die "Cannot login ", $ftp->message;

# Pass the root directory to start the crawl as the argument to the function
SearchForNative("/member_domains/yourURL/");

sub SearchForNative
{
    my $index;
    
    # Change the current working FTP directory to the path value that was passed in with the function
    $ftp->cwd($_[0]);
    
    # Create an array of the list of all the items (files and directories) in the current path
    my @directory_contents = $ftp->ls();

    # Iterate through the list of items in the current path
    for ($index = 0 ; $index < scalar @directory_contents ; $index++)
    {
        # Re-assign the current working directory to what was passed in.  THIS was the element that was missing that was preventing the code from working.
        # As the function wound down, the CWD changes but as it rewinds, it needs to be readjusted.  This line resets it to the proper value.
        $ftp->cwd($_[0]);
        
        # If the item being iterated through is named "native", then we know we've found a gallery that has NATIVE images.  This gallery will need to be SQLized later.
        # An array of these gallery types/galleries will be generated.
        if ($directory_contents[$index] eq "native")
        {
            print "Native found in " . $ftp->pwd() . "\n\n";   
        }
        
        # If the item being iterated through is a directory, then we need to call the very function we are currently in on that new directory.
        # To get the name of that new directory we take the pathname of the working directory (PWD) and append to it a / as well the new directory name.
        if ($ftp->isdir($directory_contents[$index]))
        {
            my $newdir = $ftp->pwd() . "/" . $directory_contents[$index] . "/";
            SearchForNative($newdir);
        }
    }
}