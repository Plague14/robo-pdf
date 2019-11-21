def change(fname):
    f = fname[-4:]
    fname = fname.replace(f, "")
    if (fname[-1] == ")" and fname[-3] == "("):
        n = fname[-2]
    else:
        n = "0"

    n = int(n)
    n = 2
    fname = list(fname)
    if (fname[-1] == ")" and fname[-3] == "("):
        fname[-2] = str(n)
    else:
        fname.append(" ")
        fname.append("(")
        fname.append(str(n))
        fname.append(")")

    fname = "".join(fname)
    fname = fname + f
    return fname


def verif(p, fname):
    import os.path
    while (os.path.exists(p + "/" + fname)):
        fname = change(fname)
    return p + "/" + fname


import os, PyPDF2, zipfile, shutil, time

diretorio = "D:/Projeto GD/PYTHON/robô pdf"
try:
    dirfinal = os.mkdir(diretorio + "/zips")
    os.mkdir(diretorio + "/excessoes")
    os.mkdir(diretorio + "/feitos")
except:
    OSError
cont = 0
protdel = ""
protocolo = ""
destino = diretorio + '/excessoes'
NOME1 = ""

"""
    Conta as pastas
"""
os.chdir(diretorio)
os.chdir('robo pdf')
PASTAS = os.listdir()
qntd = int(len(PASTAS))
"""
    Entra na pasta escolhida
"""
contpastas = 0
escolha = ""

for qntd in PASTAS:
    escolha = PASTAS[contpastas]
    os.chdir(diretorio + '/robo pdf/' + escolha)

    """
        Lista arquivos e pega os nomes
    """
    arquivos = os.listdir(".")  # Nome correto dos arquivos
    """
        Captura o prot e guarda na variavel prot
    """
    prot = ""
    bo = 0
    contprot = 0
    for arquivo in arquivos:
        prot = arquivos[contprot]
        confir = ' - PROT' in prot
        if confir is True:
            bo = 1
            proto = prot.split()
            protocolo = proto[0]  # Guarda o protocolo
            del arquivos[contprot]
            contprot = contprot + 1
    if bo == 0:
        try:
            os.mkdir(diretorio + '/excessoes')
        except:
            OSError
        os.chdir("D:/Projeto GD/PYTHON/robô pdf")
        shutil.move(PASTAS[contpastas], destino)
    bo = 0
    cont = 0
    contprot = 0
    """
        Eliminação de arquivos sem potencial à leitura
    """
    conthumb = 0
    for arquivo in arquivos:  # Eliminação de thumbs
        thumb = arquivos[conthumb]
        confir = 'Thumbs.db' in thumb
        if confir is True:
            del arquivos[conthumb]
        conthumb = conthumb + 1
    conthumb = 0

    contdocx = 0
    for arquivo in arquivos:  # Eliminação de DOcx
        docx = arquivos[contdocx]
        confirdocx = '.docx' in docx
        if confirdocx:
            del arquivos[contdocx]
        contdocx = contdocx + 1
    contdocx = 0

    contdocx = 0
    for arquivo in arquivos:  # Eliminação de docx abertos
        docx = arquivos[contdocx]
        confirdocx = '~$' in docx
        if confirdocx:
            del arquivos[contdocx]
        contdocx = contdocx + 1
    contdocx = 0
    """
        Salvando os arquivos com potencial a leitura na variavel que será renomeada
    """
    arquivos_originais = []
    cont1 = 0
    for arquivo in arquivos:
        arquivos_originais.append(arquivos[cont1])
        cont1 = cont1 + 1
    cont1 = 0
    """
        Renomeia para numeros para facilitar a leitura do arquivo              
    """

    countren = 0
    arquivos_renomeados = []
    for arquivo in arquivos:
        strin = str(countren)
        try:
            os.rename(arquivos[countren], "0" + strin + ".pdf")
        except:
            OSError
        arquivos_renomeados.append(str(0) + str(countren) + '.pdf')
        countren = countren + 1
    countren = 0
    """
        Ranking de resultados e decisão da abreviação
    """
    ListaTermos = [' - RE', ' - CR', ' - IMP', ' - AF', ' - CFO', ' - ASS', ' - MS', ' - RI', ' - RESP', ' - AP',
                   ' - IMP',
                   ' - ED', ' - CONT', ' - REXT', ' - AG', ' - AGI', ' - AGO']
    ListaAbrev = [
        ['RECLAMAÇÃO'],
        ['CONTRARRAZÕES', 'CONTRARRAZÃO', 'CONTRARAZÃO'],
        ['EMBARGOS A EXECUÇÃO'],
        ['ALEGAÇÕES FINAIS', 'A L E G A Ç Õ E S  F I N A I S'],
        ['CHAMADO FEITO À ORDEM', 'CHAMADO FEITO A ORDEM', 'CHAMADO A ORDEM', 'CHAMAR O FEITO À ORDEM',
         'CHAMAR O FEITO A ORDEM'],
        ['ASSUNÇÃO', 'ASSUNCAO'],
        ['MANDADO DE SEGURANÇA'],
        ['RECURSO INOMINADO'],
        ['RECURSO ESPECIAL'],
        ['APELAÇÃO', 'APELACAO'],
        ['IMPUGNAÇÃO À EXECUÇÃO', 'IMPUGNAÇÃO A EXECUÇÃO', 'IMPUGNACAO A EXECUÇÃO'],
        ['EMBARGO DE DECLARAÇÃO', 'EMBARGOS DE DECLARAÇÃO', 'EMBARAGO DE DECLARAÇÃO', 'EMBRAGO DE DECLARAÇÃO',
         'EMBRAGOS DE DECLARAÇÃO', 'EMBARGO DE DECLARACAO'],
        ['CONTESTAÇÃO', 'CONTESTACAO'],
        ['RECURSO EXTRAORDINÁRIO', 'RECURSO EXTRAORDINARIO'],
        ['AGRAVO DE INSTRUMENTO'],
        ['AGRAVO INTERNO', 'AGRAVO INOMINADO'],
        ['RECURSO DE AGRAVO', 'AGRAVO']
    ]

    """
        Leitura dos arquivos
    """

    count0 = 0
    count = 0
    count2 = 0
    count3 = 0
    sig = ""
    for arquivo in arquivos:

        pet = diretorio + 'robo pdf' + escolha + '/' + arquivos_renomeados[count0]
        lerpdf = PyPDF2.PdfFileReader(open(pet, "rb"))
        pagina = lerpdf.getPage(0)
        documento = pagina.extractText()
        documento = documento.upper()

        for arquivo in arquivos:
            for count2 in range(0, len(ListaAbrev)):
                for count3 in range(0, len(ListaAbrev[count2])):
                    texto = str(ListaAbrev[count2][count3])
                    if texto in documento:
                        sig = str(ListaTermos[count2])

    pet = None
    lerpdf = None
    """
        Colocando os nomes de volta nos arquivos
    """
    countrenome = 0
    nome_arquivo = ""
    for countrenome in range(0, len(arquivos_renomeados)):
        nome_arquivo = arquivos_originais[countrenome]
        os.rename(arquivos_renomeados[countrenome], arquivos_originais[countrenome])

    """
        Criando pasta, checkando arquivos, Tirando o prot e zipando
    """
    nome = protocolo + sig + ".zip"
    dirfinal = "D:/Projeto GD/PYTHON/robô pdf/zips/"

    arquivos1 = os.listdir()
    cont = 0

    os.chdir("D:/Projeto GD/PYTHON/robô pdf")
    verify = os.listdir(".")
    """
        Tirando arquivos desnecessarios do zip
    """
    conthumb = 0
    for arquivo in arquivos1:  # Eliminação de thumbs
        thumb = arquivos1[conthumb]
        confir = 'Thumbs.db' in thumb
        if confir is True:
            del arquivos1[conthumb]
        conthumb = conthumb + 1
    conthumb = 0

    contdocx = 0
    for arquivo in arquivos1:  # Eliminação de docx abertos
        docx = arquivos1[contdocx]
        confirdocx = '~$' in docx
        if confirdocx:
            del arquivos1[contdocx]
        contdocx = contdocx + 1
    contdocx = 0
    caminho = PASTAS[contpastas]
    contarq = 0
    os.chdir("D:/Projeto GD/PYTHON/robô pdf")
    os.chdir(caminho)
    if protocolo in verify:
        nome = verif(dirfinal, nome)
    with zipfile.ZipFile(nome, "w") as z:
        for contarq in range(0, len(arquivos1)):
            z.write(arquivos1[contarq])
    try:
        shutil.move(nome, dirfinal)
    except:
        OSError

    try:
        PyPDF2.PdfFileMerger.close(pet)
    except:
        OSError
    z.close()
    pastadel = str(PASTAS[contpastas])
    delpasta = ""
    delpasta = diretorio + '/robô pdf/' + PASTAS[contpastas]
    try:
        os.close(delpasta)
    except:
        OSError

    """
        Contagem dos feitos 
    """
    try:
        shutil.move(delpasta, diretorio + "/feitos/" + pasta, __file__)
    except:
        OSError
    try:
        os.exit()
    except:
        OSError
    try:
        os.rmdir(delpasta)
    except:
        OSError
    arquivos_renomeados = None
    print('Zipado com sucesso!')
    time.sleep(1)
    pet = None
    lerpdf = None
    pagina = None
    documento = None
    arquivos_originais = None
    arquivo = None
    arquivos = None
    arquivos1 = None
    cont = None
    countren = None
    count = None
    contarq = None
    contprot = None
    contdocx = None
    conthumb = None
    count0 = None
    count2 = None
    count3 = None
    confir = None
    confirdocx = None
    countrenome = None
    protocolo = None

    time.sleep(1)
    contpastas = contpastas + 1
