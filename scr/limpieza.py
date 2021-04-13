def download_dataset():
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle
    Returns: a folder with the downloaded and unzipped csv
    '''
    
    #Gets the name of the dataset.zip
    url = input("Introduce la url: ")
    
    #Gets the name of the dataset.zip
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]
    
    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{endopint}; say -v Monica 'descargando'"
    decompress = f"tar -xzvf {endopint}.zip; say -v Monica 'descomprimiendo'"
    delete = f"rm -rf {endopint}.zip; say -v Monica 'borrando el zip'"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    #Move the csv to uour data folder
    move_and_delete = f"mv *.csv data/dataset.csv; say -v Monica 'moviendo el dataset'"
    return os.system(move_and_delete)

def date(patron, string):
    import re
    try:
        return re.search(patron, string).group().lower()
    except:
        return f"Error"

def create(df1,column,list_):
    return df1[df1[column].isin(list_)]

def replace(datafr, list_regex, to_change, new_colum, old_column):
    datafr[new_column] = datafr[old_column].str.replace(list_regex, to_change, regex=True)
    return datafr

def limpia_precio(x):
    x = x.split("\n")
    x = x[0].split(" .")
    return x[0] + " ."