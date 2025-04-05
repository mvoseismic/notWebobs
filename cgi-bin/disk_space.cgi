#!/usr/bin/env perl
#
# Perl script to report disk space 
#
# Version 1.0
#
# Rod Stewart, UWI/SRC, 2021-07-14

use strict;

# Set test to 1 for command-line testing, 0 otherwise
my $test = 0;

# Command to get disk space
my $command = 'df -h /mnt/mvofls2/Seismic_Data /mnt/earthworm00/monitoring_data /mnt/mvofls3/Imagery_Data';

print "Content-type: text/html", "\n\n";

print "<B>Disk space on servers</B><P>\n";

print "<TT>\n";

my @status = `$command`;

@status = join( "<BR>\n", @status );

unless( $test ) {
	for (@status) {
		s/ /&nbsp;/g;
	}
}

print  @status;

print "</TT>\n";
