"""Execute notebook stages in dependency order without changing the saved benchmark."""
from pathlib import Path
import argparse, ast, copy, os, sys
import nbformat
from nbclient import NotebookClient

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'notebooks'))
from _runtime import initialize
NAMES={int(p.name[:2]):p for p in (ROOT/'notebooks').glob('*.ipynb')}
STAGES=[(1,'all'),(2,'all'),(7,'all'),(3,'all'),(4,'main'),
        (5,'rolling'),(4,'ablations'),(5,'final'),(6,'all')]

def execute(number,phase,output):
    source=NAMES[number]
    book=nbformat.read(source,4)
    cells=[copy.deepcopy(c) for c in book.cells if c.metadata.get('research_phase','all')==phase]
    part=nbformat.v4.new_notebook(cells=cells,metadata=copy.deepcopy(book.metadata))
    for c in part.cells:
        if c.cell_type=='code':c.outputs=[];c.execution_count=None
    output.mkdir(parents=True,exist_ok=True)
    target=output/f'{source.stem}_{phase}.ipynb'
    client=NotebookClient(part,timeout=None,kernel_name='python3',allow_errors=False,
                          resources={'metadata':{'path':str(ROOT)}})
    print(f'{source.name}: {phase}',flush=True)
    try:client.execute(cwd=str(ROOT))
    finally:nbformat.write(part,target)

def validate():
    assert set(NAMES)==set(range(1,8))
    for path in NAMES.values():
        book=nbformat.read(path,4);nbformat.validate(book)
        for cell in book.cells:
            if cell.cell_type=='code':ast.parse(cell.source,filename=str(path))
    print('Seven notebook files are structurally valid.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['validate','prepare','figures','train'])
    args=parser.parse_args()
    validate()
    if args.mode=='validate':sys.exit(0)
    # Use the interpreter running this command for the notebook kernel.
    os.environ['PATH']=str(Path(sys.executable).parent)+os.pathsep+os.environ.get('PATH','')
    initialize()
    output=ROOT/'.cache/executed'
    if args.mode=='prepare':
        for n,phase in STAGES[:3]:execute(n,phase,output)
    elif args.mode=='figures':
        os.environ['IAGTPF_RESULTS']='saved'
        for n in range(1,6):execute(n,'visuals',output)
    else:
        if (ROOT/'.cache/experiment/state/final_test_design_lock.json').exists():
            raise RuntimeError('A completed experiment exists. Move .cache/experiment to a separate directory before starting another full run.')
        for n,phase in STAGES:execute(n,phase,output)
        from refresh_plot_data import refresh
        refresh()
        os.environ['IAGTPF_RESULTS']='fresh'
        for n in range(1,6):execute(n,'visuals',output)
