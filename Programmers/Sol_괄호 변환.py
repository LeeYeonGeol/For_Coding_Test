def solution(p):
    answer = ''
    db = dict()
    db['('] = ')'
    db[')'] = '('
    def dfs(p):
        # 1번
        if not p:
            return p
        # 2번
        for k in range(2,len(p)+1,2):
            u = p[:k]
            v = p[k:]
            # 균형잡혔는지 검사
            if u.count('(') == u.count(')'):
                st = []
                for i in u:
                    if not st:
                        st.append(i)
                    else:
                        if st[-1] == '(' and i == ')':
                            st.pop()
                        else:
                            st.append(i)
                # 3번
                if not st:
                    return u+dfs(v)
                # 4번
                else:
                    n_p = '('+dfs(v)+')'
                    for k in u[1:-1]:
                        n_p += db[k]
                    return n_p




    return dfs(p)