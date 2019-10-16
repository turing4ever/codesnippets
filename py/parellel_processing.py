import multiprocessing as mp
import pandas as pd
import numpy as np
import requests


def test_https(domain):
    headers = {'User-Agent': 'AD-OPS-Whitelist'}
    try:
        requests.get(f'https://{domain}', headers=headers)
        return 'Pass'
    except Exception as e:
        return type(e).__name__


def process_df(df):
    print(f'{mp.current_process().name}: len={len(df)},'
          f'[{df.index.min()}, {df.index.max()}]')
    df['cd_https'] = df['campaign_domain'].apply(test_https)
    df['md_https'] = df['domain_name'].apply(test_https)
    return df


def parallelize(data, func):
    cores = mp.cpu_count()
    print(f'Running on {cores} cores')
    data_split = np.array_split(data, cores)
    pool = mp.Pool(cores)
    data = pd.concat(pool.map(func, data_split))
    pool.close()
    pool.join()
    return data


df = pd.DataFrame([{
    'domain_name': 'www.google.com',
    'campaign_domain': 'www.google.com',
} for _ in range(100)])

print(df)

if 0:
    ret = parallelize(df, process_df)
    failed = ret[(ret.cd_https != 'Pass') | (ret.md_https != 'Pass')]
    print('\n*****************')
    print(f'Found failed domains: {len(failed)}')

    if not failed.empty:
        print(failed.to_csv(index=False))
        raise ValueError('Found failed domains')

    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor() as executor:
        cores = mp.cpu_count()
        data_split = np.array_split(df, cores*5)
        print(f'Running on {cores} cores')
        ret = pd.concat(executor.map(process_df, data_split))
        failed = ret[(ret.cd_https != 'Pass') | (ret.md_https != 'Pass')]
        print('\n*****************')
        print(f'Found failed domains: {len(failed)}')
        if not failed.empty:
            print(failed.to_csv(index=False))
            raise ValueError('Found failed domains')

import concurrent.futures
#with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
with concurrent.futures.ProcessPoolExecutor(max_workers=40) as executor:
    cksize = 20
    df['cd_https'] = list(executor.map(test_https, df['campaign_domain'],
                        chunksize=cksize))
    df['md_https'] = list(executor.map(test_https, df['domain_name'],
                        chunksize=cksize))
    failed = df[(df.cd_https != 'Pass') | (df.md_https != 'Pass')]
    print('\n*****************')
    print(f'Found failed domains: {len(failed)}')
    if not failed.empty:
        print(failed.to_csv(index=False))
        raise ValueError('Found failed domains')
