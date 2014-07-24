#!perl


use LWP::UserAgent;
use WWW::Mechanize;
# 
#my $ua = LWP::UserAgent->new;
# 
## set custom HTTP request header fields
#my $req = HTTP::Request->new(GET => $server_endpoint);
#$req->header('content-type' => 'image/jpeg');
#
#
#my $resp = $ua->request($req);
#if ($resp->is_success) {
#open my $FH, '>', 'image.jpg';
#binmode $FH;
#print $FH $resp->content;
#close $FH;
#}
#else {
#    print "HTTP GET error code: ", $resp->code, "\n";
#    print "HTTP GET error message: ", $resp->message, "\n";
#}

$ua = LWP::UserAgent->new;
$server_endpoint = "http://www.cnn.com";
$req = HTTP::Request->new(GET => $server_endpoint);
$req->header('content-type' => 'image/jpeg');
$req->authorization_basic('debatable', 'opinion');

my $resp = $ua->request($req);
if ($resp->is_success)
{
	open my $FH, '>', 'c:\\ICQ\\image.jpg';
	binmode $FH;
	print $FH $resp->content;
	close $FH;
	unlink 'c:\\ICQ\\image.jpg';
}
else
{
	print "HTTP GET error code: ", $resp->code, "\n";
	print "HTTP GET error message: ", $resp->message, "\n";
}

$test_variable = "This might work?";