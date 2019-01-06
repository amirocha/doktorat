import pandas as pd

'''
DESCRIPTION: The first part of script aligns the hcn 1-0 positions to the positions of CN 1-0,
DESCRIPTION: treating CN 1-0 positions as reference ones (x + 0.537, y - 4.042)
DESCRIPTION: This has to be done, because the positions of these molecules
DESCRIPTION: don't match after convolution
DESCRIPTION: ----------
DESCRIPTION: The second part of script makes a file with the CN/HCN ratio
DESCRIPTION: Conditions: take only positions where CN and HCN and visible, 
DESCRIPTION: and both fluxes are positive (> 0) 
'''

# read the input file, and remove first 5 lines of header
hcn_positions_df = pd.read_table('serpens_hcn10_int.txt', delim_whitespace=True, header=None, skiprows = 5)

hcn_positions_df[4] =  hcn_positions_df[1] + 0.537
hcn_positions_df[5] =  hcn_positions_df[2] - 4.042

hcn_aligned_df = hcn_positions_df[[0,4,5,3]]

hcn_aligned_df.to_csv('hcn10_aligned_int.txt', sep=' ', header=None, index=False, float_format='%g')


# -----------------------


hcn_df = pd.read_table('hcn10_aligned_int.txt', delim_whitespace=True, header=None)

cn_df = pd.read_table('cn10_area.txt', delim_whitespace=True, header=None)

#pd.merge(cn_df, hcn_df, on=[1,2])

cn_hcn_df = pd.merge(cn_df, hcn_df, on=[1,2])
print(cn_hcn_df)
cn_hcn_pos_df = cn_hcn_df[(cn_hcn_df['3_x'] > 0) & (cn_hcn_df['3_y'] > 0)]
print(cn_hcn_pos_df)

cn_hcn_ratio_df = cn_hcn_pos_df['3_x'] / cn_hcn_pos_df['3_y']

final_df = pd.concat([cn_hcn_pos_df, cn_hcn_ratio_df], axis=1)[[1,2,0]]

final_df.reset_index(range(1,412), drop=True)

final_df.to_csv('ratio_cn_hcn.txt', sep=' ', header=None, float_format='%.3f')
