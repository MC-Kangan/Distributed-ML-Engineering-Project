import pandas as pd
import os

def collect_result(dirname):
    
    filename = os.path.join(dirname, 'hhr_parse_1.out')
    df = pd.read_csv(filename)
    for i in range(2, 6):
        df_new = pd.read_csv(os.path.join(dirname, f'hhr_parse_{i}.out'))
        df = pd.concat([df, df_new], axis = 0)
        
    hits_output = df[['query_id', 'best_hit']].rename({'query_id': 'fasta_id', 'best_hit': 'best_hit_id'}, axis = 1)
    hits_output.to_csv('hits_output.csv', index=False)

    df = df.dropna()
    profile_output = pd.DataFrame(data = {'ave_std': [round(df['score_std'].mean(),2)],
                                        'ave_gmean': [round(df['score_gmean'].mean(),2)]}, index = None)

    profile_output.to_csv('profile_output.csv', index=False)
    
    return None

if __name__ == "__main__":
    collect_result('/home/ec2-user/UCL_COMP0235_BIOCHEM_PROJECT/results')


