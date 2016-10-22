use CGI;
$query = new CGI;

print $query->header(-charset=>'utf-8');
print $query->start_html('Respuesta:');


if (!$query->param) {
	print $query->start_form;
    print $query->textfield(-name=>'categoria',
        -size=>40,
        -maxlength=>40);
    print $query->br;
    print $query->submit(-value=>'Submit tu categoría');
    print $query->end_form;
}
if ($query->param('categoria')){

	$categoria=$query->param('categoria');
	$filename="/home/alumnado/tmp/Categorias";
	open F, $filename or die "Imposible abrir: $!";
	$size= -s $filename;
	read(F,$buf,$size);
	close F;
	my @cat=split("\n",$buf);
	foreach my $n (@cat){
		$cat{$campos[0]}=$campos[0];	
	}
	foreach $cla(keys %cat) {
	   if($categoria =~ $cla){
			print $query->h1('Categoria:',$categoria);
			print $query->h1('Existe');
		}else{
			print $query->h1('Categoria:',$categoria);
			print $query->h1('No existe');
		}
	}
}

print $query->end_html;