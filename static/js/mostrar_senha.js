function mostrarSenha(){

	var tipo = document.getElementById('inputPassword');
	const btn = document.querySelector('.myimg');

	if (tipo.type == 'password') 
	{
		tipo.type = 'text'
		btn.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8SA14-A-zoRaiJ2GdUiESsisaFiHNYrUZtjtjZqnth0D_KdfkwzQWIdCjbzhAoYKPTvs&usqp=CAU'
	}
	else
	{
		tipo.type = 'password'
		btn.src = 'https://icon-library.com/images/icon-eyes/icon-eyes-12.jpg'
	}
}