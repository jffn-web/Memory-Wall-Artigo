import re, math, statistics
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DADOS = BASE / "dados" / "brutos"
SAIDA = BASE / "dados" / "processados"
SAIDA.mkdir(parents=True, exist_ok=True)

T_CRIT_95_DF29 = 2.045
ARQUIVOS = [("mbw16.txt", "16 MiB"), ("mbw128.txt", "128 MiB"), ("mbw1024.txt", "1024 MiB")]

def extrair_memcpy(path):
    texto = path.read_text(encoding="utf-8", errors="ignore")
    return [float(x) for x in re.findall(r"AVG\s+Method:\s+MEMCPY\s+Elapsed:\s+[0-9.]+\s+MiB:\s+[0-9.]+\s+Copy:\s+([0-9.]+) MiB/s", texto)]

linhas = ["tamanho_array,n,media_mib_s,desvio_padrao,ic95"]
for arquivo, rotulo in ARQUIVOS:
    valores = extrair_memcpy(DADOS / arquivo)
    n = len(valores)
    media = statistics.mean(valores)
    desvio = statistics.stdev(valores)
    ic95 = T_CRIT_95_DF29 * desvio / math.sqrt(n)
    linhas.append(f"{rotulo},{n},{media:.4f},{desvio:.4f},{ic95:.4f}")

(SAIDA / "largura_banda_estatistica.csv").write_text("\n".join(linhas) + "\n", encoding="utf-8")
print("Arquivo gerado em dados/processados/largura_banda_estatistica.csv")
