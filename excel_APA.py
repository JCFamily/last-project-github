import pandas as pd
df=pd.read_excel('apa_ref.xlsx')

print('저자.(년도).제목.저널명,권(호),페이지. DOI')

ref=df.loc[:,['저자','발행년','제목(원문)','학술지','권','호','시작페이지','끝페이지','DOI']]
print(ref.head())


ref['year']=ref['발행년'].astype(str)
ref['vol']=ref['권'].astype(str);ref['no']=ref['호'].astype(str)
ref['s']=ref['시작페이지'].astype(str);ref['e']=ref['끝페이지'].astype(str)
ref['vol(no)']=ref[['vol','no']].apply(lambda x:'('.join(x),axis=1)
ref['pp']=ref[['s','e']].apply(lambda x:'-'.join(x),axis=1)
ref['p1']=ref[['저자','year']].apply(lambda x: '.('.join(x),axis=1)
ref['p2']=ref[['p1','제목(원문)']].apply(lambda x:'). '.join(x),axis=1)
ref['p3']=ref[['p2','학술지']].apply(lambda x:'. '.join(x),axis=1)
ref['p4']=ref[['p3','vol(no)']].apply(lambda x:', '.join(x),axis=1)
ref['p5']=ref[['p4','pp']].apply(lambda x:'), '.join(x),axis=1)
ref['p6']=ref[['p5','DOI']].apply(lambda x:'. '.join(x),axis=1)
print(ref['p6'].head())

ref['p6'].to_csv("result.csv")
