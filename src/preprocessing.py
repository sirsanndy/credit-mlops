import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder

def ohe_transform(dataset: pd.DataFrame, subset: str, prefix: str, ohe: OneHotEncoder):
    """
    Fungsi untuk melakukan encoding data kategorik dengan OneHotEncoder.
    
    Parameters:
    dataset : pd.DataFrame
        Set data yang ingin dilakukan pengkodean.
    subset : str
        Nama kolom yang terdapat pada data di parameter dataset.
    prefix : str
        Nama awalan yang akan disematkan pada kolom hasil pengkodean.
    ohe : OneHotEncoder
        Encoder yang sebelumnya telah dilatih oleh data kategorik khusus.
    """
    
    # Validasi parameter
    if not isinstance(dataset, pd.DataFrame):
        raise RuntimeError("Fungsi ohe_transform: parameter dataset harus bertipe DataFrame!")
    
    if not isinstance(ohe, OneHotEncoder):
        raise RuntimeError("Fungsi ohe_transform: parameter ohe harus bertipe OneHotEncoder!")
    
    if not isinstance(prefix, str):
        raise RuntimeError("Fungsi ohe_transform: parameter prefix harus bertipe str!")
    
    if not isinstance(subset, str):
        raise RuntimeError("Fungsi ohe_transform: parameter subset harus bertipe str!")
    
    try:
        _ = dataset.columns.tolist().index(subset)
    except:
        raise RuntimeError("Fungsi ohe_transform: parameter subset string namun data tidak ditemukan dalam daftar kolom yang terdapat pada parameter dataset.")
    
    print("Fungsi ohe_transform: parameter telah divalidasi.")
    
    # Duplikasi data
    dataset = dataset.copy()
    
    # Print daftar nama kolom sebelum pengkodean
    print(f"Fungsi ohe_transform: daftar nama kolom sebelum dilakukan pengkodean adalah {list(dataset.columns)}.")
    
    # List comprehension untuk menyimpan nama kolom hasil pengkodean
    col_names = [f"{prefix}_{col_name}" for col_name in ohe.categories_[0].tolist()]
    
    # Proses pengkodean
    encoded = pd.DataFrame(ohe.transform(dataset[[subset]]).toarray(), columns=col_names, index=dataset.index)
    
    # Penyatuan hasil pengkodean dengan data sebelum pengkodean
    dataset = pd.concat([dataset, encoded], axis=1)
    
    # Penghapusan kolom asli yang telah dikodekan
    dataset.drop(columns=[subset], inplace=True)
    
    # Print daftar nama kolom setelah pengkodean
    print(f"Fungsi ohe_transform: daftar nama kolom setelah dilakukan pengkodean adalah {list(dataset.columns)}.")
    
    return dataset