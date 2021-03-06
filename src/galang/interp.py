from typing import Union, Optional, Dict, List, Any, Callable, NamedTuple
from dataclasses import dataclass
from numpy import ndarray
from copy import copy, deepcopy
from galang.types import (Expr, Ref, Ap, Val, Const, Lam, Intrin, MethodName,
                          TMap, Tuple, Let, IExpr, Lib, IMem, IVal, ILam)


import numpy as np

def interp(expr:Expr, lib:Lib, m:IMem)->Tuple[IExpr,IMem]:
  if isinstance(expr, Val):
    if isinstance(expr.val, Ref):
      return (m[expr.val],m)
    elif isinstance(expr.val, Const):
      return (IVal(expr.val.const), m)
    else:
      raise ValueError(f"Invalid value {expr}")
  elif isinstance(expr, Let):
    val,m2 = interp(expr.expr, lib, m)
    return interp(expr.body, lib, m2.set(expr.ref,val))
  elif isinstance(expr, Ap):
    func,m2 = interp(expr.func, lib, m)
    arg,m3 = interp(expr.arg, lib, m2)
    if isinstance(func, ILam):
      return interp(func.body, lib, m3.set(Ref(func.name),arg))
    else:
      raise ValueError(f"Invalid callable {func}")
  elif isinstance(expr, Lam):
    return (ILam(expr.name, expr.body),m)
  elif isinstance(expr, Intrin):
    libentry = lib[expr.name]
    iargs = {}
    for aname,aexpr in expr.args.items():
      a,_ = interp(aexpr, lib, m)
      iargs.update({aname: a})
    return (libentry.impl(iargs), m)
  else:
    raise ValueError(f"Invalid expression {expr}")


