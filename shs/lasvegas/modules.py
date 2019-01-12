
def get_combs(cases, prior=[], root=True):
    if cases:
        cases, prior, prior_ = cases.copy(), prior.copy(), prior.copy()
        prior_.append(cases.pop())
        combs = [*get_combs(cases, prior, False),
                 *get_combs(cases, prior_, False)]
    else:
        return [prior]
    if root:
        combs = sorted([tuple(sorted(ls)) for ls in combs])
        combs = sorted([list(t) for t in combs], key=lambda x: len(x))
    return combs
