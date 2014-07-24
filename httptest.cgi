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

#my $url = "http://upload.wikimedia.org/wikipedia/en/7/70/Blogscope-logo-simple.jpg";
##my $cookie_jar;
#
#my $mech = WWW::Mechanize->new();
#$mech->get($url);
#
#$mech->success() or die "Can't fetch the Requested page";
#my $val = $mech->content;
#print $val;


        $ua = LWP::UserAgent->new;
        $server_endpoint = "http://www.cnn.com";
        $req = HTTP::Request->new(GET => $server_endpoint);
        $req->header('content-type' => 'image/jpeg');
        $req->authorization_basic('rafal1423', 'rafal1243');
        
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