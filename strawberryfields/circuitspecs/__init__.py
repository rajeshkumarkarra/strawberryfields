# Copyright 2019 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Circuit specifications
======================

**Module name:** :mod:`strawberryfields.circuitspecs`

.. currentmodule:: strawberryfields.circuitspecs

This subpackage implements the :class:`CircuitSpecs` class, an abstract base class
used to define classes or families of quantum circuits, e.g., circuits that can be executed on particular
hardware or simulator backends.

The information in the ``CircuitSpecs`` instances is used by :meth:`.Program.compile` to validate and
compile quantum programs. By querying the ``CircuitSpecs`` class representing the requested compilation
target, ``Program.compile`` can

1. **Validate** that the Program has the correct number of modes, and consists
   of valid quantum operations in the correct topology for the targeted circuit class.

2. **Compile** the Program into an :term:`equivalent circuit` that has the topology required by the
   targeted circuit class, decomposing circuit operations as required.

Note that the compilation process is not perfect and can provide false negatives: it can admit
failure by raising a :class:`.CircuitError` even if the Program theoretically is equivalent to a
circuit that belongs in the target circuit class.


Data members
------------

.. autosummary::
   circuit_db

The circuit class database :attr:`circuit_db` is a dictionary mapping the circuit family
short name to the corresponding CircuitSpecs instance.
In particular, for each backend supported by Strawberry Fields the database contains a
corresponding CircuitSpecs instance with the same short name, used to validate Programs to be
executed on that backend.


.. currentmodule:: strawberryfields.circuitspecs.circuit_specs

Classes
-------

.. autosummary::
   CircuitSpecs


CircuitSpecs methods
--------------------

.. currentmodule:: strawberryfields.circuitspecs.circuit_specs.CircuitSpecs

.. autosummary::
   modes
   local
   remote
   interactive
   primitives
   decompositions
   parameter_ranges
   graph
   circuit
   compile


Code details
~~~~~~~~~~~~
"""
from .circuit_specs import CircuitSpecs
from .chip0 import Chip0Specs
from .fock import FockSpecs
from .gaussian import GaussianSpecs
from .gbs import GBSSpecs
from .tensorflow import TFSpecs


specs = (Chip0Specs, FockSpecs, GaussianSpecs, GBSSpecs, TFSpecs)

circuit_db = {c.short_name: c for c in specs}
"""dict[str, ~strawberryfields.circuitspecs.CircuitSpecs]: Map from circuit family short name to the corresponding class."""

__all__ = ["circuit_db", "CircuitSpecs"]
