<br />

![Pixel Bootstrap PRO - Full-Stack Starter gerado pelo AppSeed](https://user-images.githubusercontent.com/51070104/168760719-f0e45406-2b2a-43e0-badf-fa953edb62b8.png)

<br />

## ✨ Estrutura da base de código

O projeto é codificado usando uma estrutura simples e intuitiva apresentada a seguir:

```bash
<PROJETO RAIZ>
    |
    |-- core/ # Implementa a configuração do aplicativo
    | |-- settings.py # Define configurações globais
    | |-- wsgi.py # Inicia o aplicativo em produção
    | |-- urls.py # Definir URLs servidos por todos os aplicativos/nós
    |
    |-- aplicativos/
    | |
    | |-- home/ # Um aplicativo simples que serve arquivos HTML
    | | |-- views.py # Serve páginas HTML para usuários autenticados
    | | |-- urls.py # Defina algumas rotas super simples
    | |
    | |-- authentication/ # Lida com rotas de autenticação (login e registro)
    | | |-- urls.py # Definir rotas de autenticação
    | | |-- views.py # Lida com login e registro
    | | |-- forms.py # Definir formulários de autenticação (login e registro)
    | |
    | |-- estático/
    | | |-- <css, JS, imagens> # arquivos CSS, arquivos Javascripts
    | |
    | |-- templates/ # Modelos usados para renderizar páginas
    | |-- includes/ # Blocos e componentes HTML
    | | |-- navigation.html # Componente do menu principal
    | | |-- sidebar.html # Componente da barra lateral
    | | |-- footer.html # App Footer
    | | |-- scripts.html # Scripts comuns a todas as páginas
    | |
    | |-- layouts/ # páginas mestras
    | | |-- base-fullscreen.html # Usado por páginas de autenticação
    | | |-- base.html # Usado por páginas comuns
    | |
    | |-- contas/ # páginas de autenticação
    | | |-- login.html # Página de login
    | | |-- register.html # Página de registro
    | |
    | |-- home/ # Páginas do kit de interface do usuário
    | |-- index.html # Página de índice
    | |-- 404-page.html # 404 página
    | |-- *.html # Todas as outras páginas
    |
    |-- requisitos.txt # Módulos de desenvolvimento - armazenamento SQLite
    |
    |-- .env # Injetar configuração via ambiente
    |-- manage.py # Inicia o aplicativo - script de inicialização padrão do Django
    |
    |-- *********************************************** *************
```

