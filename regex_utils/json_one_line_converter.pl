#!/usr/bin/perl

# Convert json file to json body command for curl request
use strict;
use warnings;

while (<>) {
    my $var = $_;
    chomp $var;
    $var =~ s/\s+//g;
    $var =~ s/ (\") /\\$1/xg;
    print $var;
}