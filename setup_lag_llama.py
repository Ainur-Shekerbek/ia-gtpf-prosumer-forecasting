"""Install the optional isolated baseline and its fixed upstream checkpoint."""
from pathlib import Path
import hashlib, json, os, subprocess, sys, urllib.request, venv

ROOT=Path(__file__).resolve().parent
ENV=ROOT/'.venv_lag_llama'
if __name__=='__main__':
    venv.EnvBuilder(with_pip=True).create(ENV)
    python=ENV/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
    subprocess.run([str(python),'-m','pip','install','-r',str(ROOT/'requirements-lag-llama.txt')],check=True)
    info=json.loads((ROOT/'dataset/config/lag_llama_checkpoint.json').read_text())
    target=ROOT/info['checkpoint'];target.parent.mkdir(parents=True,exist_ok=True)
    if not target.exists():
        url=f'https://huggingface.co/{info["repository"]}/resolve/{info["revision"]}/lag-llama.ckpt'
        temporary=target.with_suffix('.download')
        urllib.request.urlretrieve(url,temporary)
        if hashlib.sha256(temporary.read_bytes()).hexdigest()!=info['sha256']:
            raise ValueError('Downloaded checkpoint checksum differs from the recorded experiment')
        temporary.replace(target)
    assert hashlib.sha256(target.read_bytes()).hexdigest()==info['sha256']
    print('Lag-Llama environment and checkpoint are ready.')
