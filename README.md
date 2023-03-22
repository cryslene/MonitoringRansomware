# MonitoringRansomware
Projeto realizado com fins totalmente acadêmicos, para monitoração, análise e detecção de ataques Ransomware em sistemas linux.
Defendido em TCC para conclusão do curso de Engenharia de Computação pela UFPA, apresentado no Simpósio Brasileiro De Segurança Da Informação E De Sistemas Computacionais (SBSEG) e publicado na Biblioteca Digital da SBC (SBC OpenLib – SOL).


Sobre os códigos:
- encrypt.py -> Simulação do Ransomware - criptografa ou descriptografa a pasta "files" (a senha de descriptografia está no código).
- inotify_detected_ransom.py -> Monitoração e identificação do Ransomware com inotify e file.
- strace_detected_ransom.py -> Monitoração e identificação do Ransomware com strace.
- Discovery.py e Crypter.py -> Arquivos de importação para execução do código que simula o Ransomware no arquivo "encrypt.py"

Exemplo de teste: Executar o código "inotify_detected_ransom.py" para monitorar em uma janela do terminal e iniciar a simulação do Ransomware com a execução do código "encrypt.py" em outro terminal.
* O comando "python3 encrypt.py" executa o código do Ransomware para criptografar
* O comando "python3 encrypt.py -d" executa o código do Ransomware para descriptografar
