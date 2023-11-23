<h2>Sistema Automático de Registros de protudos</h2>

<h2>Objetivo</h2>
<p>Esse repositório tém como objetivo o meu aprendizado em automação de coisas utilizando python</p>

<h2>Conteúdo do Repositório</h2>
<h3>Script de Automação com PyAutoGui</h3>
 <p>
        Este script Python, denominado <code>app.py</code>, utiliza a biblioteca PyAutoGUI para automatizar tarefas relacionadas ao processo de registro de produtos.
</p>

 <h3>Credenciais de Login:</h3>

 <ul>
        <li>O código utiliza <code>pyautogui.click</code> para clicar em posições específicas da tela (representadas pelos valores x, y) e <code>pyautogui.write</code> para inserir texto.</li>
        <li>Clica em uma posição específica e insere o nome de usuário ('jhonatan').</li>
        <li>Clica em outra posição e insere a senha ('123456').</li>
        <li>Clica em uma terceira posição para fazer o login.</li>
</ul>

<h3>Leitura de Arquivo de Produtos:</h3>

 <ul>
        <li>Obtém o caminho absoluto para o arquivo '<code>produtos.txt</code>'.</li>
        <li>Utiliza um bloco <code>with open</code> para abrir o arquivo no modo leitura ('r').</li>
        <li>Itera sobre as linhas do arquivo, que contêm informações sobre produtos separadas por vírgulas.</li>
    </ul>


  <h3>Registro de Produtos:</h3>

  <ul>
        <li>Para cada linha do arquivo:</li>
        <ul>
            <li>Extrai as informações do produto, quantidade e preço.</li>
            <li>Clica em posições específicas para inserir as informações nos campos apropriados.</li>
            <li>Clica em uma posição para registrar o produto.</li>
            <li>Aguarda por 1 segundo usando <code>sleep(1)</code> antes de prosseguir para o próximo produto.</li>
        </ul>
    </ul>


<p>
        É importante notar que as posições específicas (<code>x</code>, <code>y</code>) usadas no código (<code>pyautogui.click</code>) são coordenadas na tela e devem ser ajustadas de acordo com a resolução e o layout da tela do sistema onde o script será executado. Se essas posições não estiverem corretas, a automação pode não funcionar conforme o esperado.
    </p>

<h2>Como Contribuir</h2>
<p>Sinta-se à vontade para explorar este repositório, clonar os projetos, fazer melhorias ou sugerir correções. Se você tiver qualquer dúvida ou feedback sobre o código ou os conceitos apresentados, fique à vontade para abrir uma issue ou enviar um pull request.</p>

<h2>Aviso</h2>
<p>É importante ressaltar que, como estudante e aprendiz, posso cometer erros no código ou na compreensão dos conceitos. Este repositório é destinado a fins educacionais e de aprendizado mútuo.</p>
