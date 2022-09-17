def execute_param_fn (abc_list,hosei,param_fn):
    return param_fn(abc_list,hosei)

if __name__ == "__main__":
    print (execute_param_fn([1,2,3],4, lambda x ,y:max(x) + y))
    print (execute_param_fn([1,2,3],4, lambda x ,y:min(x) - y))