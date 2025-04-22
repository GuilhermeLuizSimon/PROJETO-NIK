<?php

// aguarda o php receber o áudio vindo do esp32

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Salvar o áudio enviado
    $target_dir = "NIK/SongSaver/";
    if (!is_dir($target_dir)) {
        mkdir($target_dir, 0777, true);
    }

    $nomeArquivo = uniqid() . ".wav"; // Cria um nome único
    $caminhoCompleto = $target_dir . $nomeArquivo;

    // pega os dados vindo do POST
    $rawData = file_get_contents("php://input");

    // executa a criação do arquivo de áudio e checagem
    if (file_put_contents($caminhoCompleto, $rawData)) {
        
        // executar o script do python para que ele crie o audio resposta.wav

        // espaceshellcmd e escapeshellarg podem ser substituídos pelo shell_exec,
        // mas foram colocados por segurança de caracteres especiais
        $command = escapeshellcmd("python3 process_audio.py " . escapeshellarg($caminhoCompleto));
        $resultado = shell_exec($command);

         // Retornar resposta de áudio ao esp32
        $respostaAudio = "NIK/Esp32/resposta.wav"; // caminho do arquivo a ser devolvido

        // verifica se o arquivo existe
        if (file_exists($respostaAudio)) {

            // envio de audio
            header("Content-Type: audio/wav");      // ou outro tipo correto do arquivo
            header("Content-Length: " . filesize($respostaAudio));
            readfile($respostaAudio);
            exit;
        } else {

            ErrorAudio();
        }
    } else {
        ErrorAudio();
    }
} else {
    ErrorAudio();
}

function ErrorAudio(){
    // Definir o tipo de conteúdo como áudio WAV
    header("Content-Type: audio/wav");

    // Caminho para o arquivo de áudio de erro
    $error_audio_path = "audios/error_audio.wav";
    
    // Verificar se o arquivo de erro existe
    if (file_exists($error_audio_path)) {
        // Ler e enviar o arquivo de áudio
        readfile($error_audio_path);
    } else {
        // Caso o arquivo de erro não exista, enviar um código de erro HTTP 500
        http_response_code(500);
        echo "Erro interno do servidor: áudio de erro não encontrado.";
    }
}

