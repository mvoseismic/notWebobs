#!/usr/bin/env perl
#
# R.C Stewart, Nov 2024
# based on script by 
# Arvid Ramdeane, Nov 2024

# Variables and Definitions

use strict;
use warnings;
use CGI;
use CGI::Carp qw/fatalsToBrowser/;
use Time::Local;
use File::Basename;
use File::Copy;
use List::Util qw[min max];


# CGI Object
my $q = CGI->new;

# HTTP header
print $q->header;

print $q->start_html(	-title => "Megaplot",
			-head => [$q->meta( {-http_equiv=>'REFRESH',-content=>'60'} )], 
		      	-script => 
				[
					{ -language => 'javascript', -src => "/JavaScripts/jquery.js"},
				],
	);
	
	# check of url string contain params
	if ($q->param)
	{
		# get all params and print
		# write to file
		my @param_names = $q->param;
		print $q->h2("You submitted:");

		# write to file
		#open(FH, ">", "/mvo/webobs/WWW/html/megaplot.txt") or die $!;
		open(FH, ">", "/var/www/html/configMegaplotWebobs.m") or die $!;

		foreach my $name (@param_names)
		{
			# print to browser
			my $param_value = $q->param($name);
			print ("
				<p><b>$name</b>: <span>$param_value</span></p>
			");

			# write to file
			my $file_str = "$name: $param_value\n";
			print FH $file_str;
			#print $q->p($q->param($name));
		}
		
		close(FH) or die;
	}	
	
	# form
	print $q->h1({-style=>"color:red;"}, "Test Form");
	print("
		<form action='/cgi-bin/fetchMegaplot.cgi' method='get'>
			<label for='fname'>First name:</label><br>
			<input type='text' id='fname' name='fname' required><br>
			<label for='lname'>Last name:</label><br>
                        <input type='text' id='lname' name='lname' required><br>
			<input type='submit' value='Submit'>
		</form>
	");

print $q->end_html, "\n";

