mod_0 = sm.tsa.statespace.SARIMAX(
        df_train.iloc[:,0],
        order=(0,1,1),
        seasonal_order=(0,1,1,6),
        enforce_stationarity=False,
        enforce_invertibility=False)
results_0 = mod_0.fit()

mod_1 = sm.tsa.statespace.SARIMAX(
        df_train.iloc[:,1],
        order=(0,1,1),
        seasonal_order=(0,1,1,6),
        enforce_stationarity=False,
        enforce_invertibility=False)
results_1 = mod_1.fit()

mod_2 = sm.tsa.statespace.SARIMAX(
        df_train.iloc[:,2],
        order=(0,1,1),
        seasonal_order=(0,1,1,6),
        enforce_stationarity=False,
        enforce_invertibility=False)
results_2 = mod_2.fit()

exp_1 = SimpleExpSmoothing(df_train.iloc[:,0], 
                           initialization_method='estimated').fit()
exp_1_foc = exp_1.forecast(20).rename(r'$\alpha%s$'%exp_1.model.params['smoothing_level'])

exp_2 = SimpleExpSmoothing(df_train.iloc[:,1], 
                           initialization_method='estimated').fit()
exp_2_foc = exp_2.forecast(20).rename(r'$\alpha=%s$'%exp_2.model.params['smoothing_level'])

exp_3 = SimpleExpSmoothing(df_train.iloc[:,2], 
                           initialization_method='estimated').fit()
exp_3_foc = exp_3.forecast(20).rename(r'$\alpha=%s$'%exp_3.model.params['smoothing_level'])
exp_4 = SimpleExpSmoothing(df_train.iloc[:,3], 
                           initialization_method='estimated').fit()
exp_4_foc = exp_4.forecast(20).rename(r'$\alpha=%s$'%exp_3.model.params['smoothing_level'])