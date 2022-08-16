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

function Senha(){

	var senha = document.getElementById('inputPassword1');
	const botao = document.querySelector('.myimg1');

	if (senha.type == 'password') 
	{
		senha.type = 'text'
		botao.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8SA14-A-zoRaiJ2GdUiESsisaFiHNYrUZtjtjZqnth0D_KdfkwzQWIdCjbzhAoYKPTvs&usqp=CAU'
	}
	else
	{
		senha.type = 'password'
		botao.src = 'https://icon-library.com/images/icon-eyes/icon-eyes-12.jpg'
	}
}

function showSenha(){

	var password = document.getElementById('inputPassword2');
	const button = document.querySelector('.myimg2');

	if (password.type == 'password') 
	{
		password.type = 'text'
		button.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8SA14-A-zoRaiJ2GdUiESsisaFiHNYrUZtjtjZqnth0D_KdfkwzQWIdCjbzhAoYKPTvs&usqp=CAU'
	}
	else
	{
		password.type = 'password'
		button.src = 'https://icon-library.com/images/icon-eyes/icon-eyes-12.jpg'
	}
}

function registrarPassword(){

	var registrar = document.getElementById('inputPassword3');
	const press = document.querySelector('.myimg3');

	if (registrar.type == 'password') 
	{
		registrar.type = 'text'
		press.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8SA14-A-zoRaiJ2GdUiESsisaFiHNYrUZtjtjZqnth0D_KdfkwzQWIdCjbzhAoYKPTvs&usqp=CAU'
	}
	else
	{
		registrar.type = 'password'
		press.src = 'https://icon-library.com/images/icon-eyes/icon-eyes-12.jpg'
	}
}