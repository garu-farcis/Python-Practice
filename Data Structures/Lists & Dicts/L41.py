"""Given a pandas DataFrame, coerce amount to float (invalid → NaN),
 create status = "high" if amount > 100 else "normal", and drop rows where amount is null after coercion."""