
# CPX Monitoring Tool

**How to Install**

```bash
git clone https://github.com/indraneelmax/cpx_monitor

cd cpx_monitor

python -m venv testenv

source testenv/bin/activate

pip install .

which cpx_monitor

```
**How to Run**

```
%> cpx_monitor --help

Welcome to CPX Monitoring Tool - v0.1.0
usage: cpx_monitor [-h] [--avg_per_service] [--track_services [TRACK_SERVICES ...]] [--min_hosts [MIN_HOSTS]] [base_url]

A simple cpx server monitoring tool.

positional arguments:
  base_url              URL for the CPX Monitoring service

options:
  -h, --help            show this help message and exit
  --avg_per_service     List services by type with their average cpu/mem usage.
  --track_services [TRACK_SERVICES ...]
                        Track cpu/mem usage of a given service
  --min_hosts [MIN_HOSTS]
                        Services with hosts greater than min_hosts will be marked as needs attention.
```
**Example Run**
```
http://localhost:5500 is the url to our CPX Monitoring service for our examples

# Example-1 : List avg cpu/memory usage per service

%> cpx_monitor http://localhost:5500  --avg_per_service

Welcome to CPX Monitoring Tool - v0.1.0
Listing services - 
+--------------------+---------+------------+
|      Service       | AVG CPU | AVG MEMORY |
+--------------------+---------+------------+
|     MLService      |  48.75% |   45.06%   |
|     IdService      |  54.33% |   52.48%   |
| PermissionsService |  50.40% |   59.40%   |
|     GeoService     |  50.24% |   51.65%   |
|    RoleService     |  43.52% |   50.80%   |
|    AuthService     |  38.88% |   56.71%   |
|   TicketService    |  38.88% |   54.12%   |
|   StorageService   |  43.38% |   47.38%   |
|    TimeService     |  60.70% |   52.40%   |
|    UserService     |  57.90% |   37.70%   |
+--------------------+---------+------------+

# Example-2 : Track cpu/memory usage of given list of services

%> cpx_monitor --track_services UserService TimeService

+-------------+-------------+------+--------+
|      IP     |   Service   | CPU  | MEMORY |
+-------------+-------------+------+--------+
|  10.58.1.2  | TimeService | 14%  |  36%   |
|  10.58.1.58 | TimeService |  2%  |  80%   |
|  10.58.1.38 | TimeService | 100% |  25%   |
|  10.58.1.37 | TimeService | 75%  |  73%   |
|  10.58.1.23 | TimeService | 43%  |  44%   |
| 10.58.1.110 | TimeService | 33%  |  38%   |
|  10.58.1.45 | TimeService | 96%  |  65%   |
|  10.58.1.85 | TimeService | 31%  |  10%   |
| 10.58.1.139 | TimeService |  3%  |  14%   |
|  10.58.1.32 | TimeService | 65%  |  73%   |
|  10.58.1.70 | UserService | 41%  |  15%   |
| 10.58.1.141 | UserService | 94%  |  95%   |
| 10.58.1.131 | UserService | 93%  |  33%   |
|  10.58.1.31 | UserService | 26%  |  64%   |
| 10.58.1.149 | UserService | 22%  |  86%   |
| 10.58.1.121 | UserService |  3%  |  37%   |
| 10.58.1.143 | UserService |  1%  |  88%   |
|  10.58.1.77 | UserService | 85%  |  83%   |
|  10.58.1.98 | UserService | 29%  |  74%   |
|  10.58.1.52 | UserService | 23%  |  56%   |
+-------------+-------------+------+--------+
Do you really want to exit? y/n 
y
Exiting...

# Example-3 : List cpu/memory usage of all hosts across services

%> cpx_monitor

Welcome to CPX Monitoring Tool - v0.1.0
+-------------+--------------------+-----+--------+
|      IP     |      Service       | CPU | MEMORY |
+-------------+--------------------+-----+--------+
|  10.58.1.55 |     MLService      | 70% |  74%   |
|  10.58.1.29 |     MLService      | 64% |  24%   |
|  10.58.1.11 |     MLService      | 21% |  21%   |
|  10.58.1.17 |     MLService      | 60% |  77%   |
| 10.58.1.106 |     MLService      | 98% |  96%   |
|  10.58.1.76 |     MLService      | 63% |  26%   |
|  10.58.1.93 |     MLService      |  7% |  76%   |
|  10.58.1.42 |     MLService      | 75% |  79%   |
|  10.58.1.66 |     MLService      | 32% |   7%   |
| 10.58.1.103 |     MLService      | 47% |   8%   |
|  10.58.1.3  |     MLService      | 90% |  86%   |
| 10.58.1.118 |     MLService      | 45% |  65%   |
|  10.58.1.63 |     MLService      | 60% |  34%   |
| 10.58.1.134 |     MLService      | 10% |  16%   |
|  10.58.1.79 |     MLService      | 16% |  55%   |
|  10.58.1.19 |     MLService      | 35% |  11%   |
|  10.58.1.64 |     IdService      | 43% |  62%   |
|  10.58.1.92 |     IdService      | 13% |  88%   |
|  10.58.1.30 |     IdService      | 96% |  24%   |
| 10.58.1.117 |     IdService      | 15% |  81%   |
| 10.58.1.120 |     IdService      | 41% |  56%   |
|  10.58.1.62 |     IdService      | 96% |  21%   |
|  10.58.1.51 |     IdService      | 51% |  96%   |
| 10.58.1.142 |     IdService      | 96% |  100%  |
| 10.58.1.125 |     IdService      | 27% |  68%   |
|  10.58.1.16 |     IdService      | 48% |  83%   |
|  10.58.1.40 |     IdService      | 56% |  18%   |
|  10.58.1.71 |     IdService      | 39% |   0%   |
| 10.58.1.112 |     IdService      | 66% |  73%   |
|  10.58.1.14 |     IdService      |  3% |  99%   |
|  10.58.1.78 |     IdService      | 55% |  85%   |
| 10.58.1.123 |     IdService      | 87% |  22%   |
|  10.58.1.86 |     IdService      | 74% |  13%   |
|  10.58.1.24 |     IdService      | 88% |  39%   |
|  10.58.1.96 |     IdService      | 69% |  20%   |
| 10.58.1.116 |     IdService      | 52% |  79%   |
| 10.58.1.133 |     IdService      | 14% |  54%   |
|  10.58.1.12 | PermissionsService | 96% |  49%   |
| 10.58.1.150 | PermissionsService | 94% |   4%   |
|  10.58.1.47 | PermissionsService | 84% |  14%   |
| 10.58.1.128 | PermissionsService | 37% |  51%   |
| 10.58.1.127 | PermissionsService | 55% |  52%   |
|  10.58.1.36 | PermissionsService |  5% |  21%   |
|  10.58.1.65 | PermissionsService | 95% |  36%   |
| 10.58.1.140 | PermissionsService | 81% |  57%   |
| 10.58.1.130 | PermissionsService | 78% |  65%   |
|  10.58.1.87 | PermissionsService | 26% |   5%   |
|  10.58.1.94 |     GeoService     | 57% |  10%   |
|  10.58.1.44 |     GeoService     | 70% |  34%   |
|  10.58.1.33 |     GeoService     | 25% |  11%   |
| 10.58.1.148 |     GeoService     | 56% |  85%   |
| 10.58.1.122 |     GeoService     | 66% |  98%   |
| 10.58.1.115 |     GeoService     | 83% |  88%   |
| 10.58.1.138 |     GeoService     |  2% |  15%   |
|  10.58.1.67 |     GeoService     | 63% |  18%   |
| 10.58.1.144 |     GeoService     | 44% |  72%   |
|  10.58.1.91 |     GeoService     | 51% |  86%   |
| 10.58.1.108 |     GeoService     | 29% |  85%   |
|  10.58.1.20 |     GeoService     | 90% |  15%   |
| 10.58.1.126 |     GeoService     | 30% |  37%   |
|  10.58.1.26 |     GeoService     | 81% |  97%   |
|  10.58.1.59 |     GeoService     | 71% |  72%   |
| 10.58.1.119 |     GeoService     |  5% |  39%   |
|  10.58.1.68 |     GeoService     | 84% |  11%   |
|  10.58.1.41 |    RoleService     | 65% |  73%   |
|  10.58.1.90 |    RoleService     | 85% |   3%   |
|  10.58.1.21 |    RoleService     | 60% |  52%   |
|  10.58.1.80 |    RoleService     | 74% |  80%   |
|  10.58.1.18 |    RoleService     | 59% |  98%   |
| 10.58.1.132 |    RoleService     | 54% |  13%   |
|  10.58.1.10 |    RoleService     | 51% |  79%   |
|  10.58.1.75 |    RoleService     |  3% |  74%   |
|  10.58.1.49 |    RoleService     | 94% |  23%   |
| 10.58.1.124 |    RoleService     | 31% |  26%   |
| 10.58.1.100 |    RoleService     | 44% |  57%   |
|  10.58.1.54 |    RoleService     | 53% |  11%   |
| 10.58.1.105 |    RoleService     | 47% |  39%   |
|  10.58.1.97 |    RoleService     | 81% |  78%   |
|  10.58.1.27 |    RoleService     | 49% |  95%   |
|  10.58.1.7  |    RoleService     | 98% |  44%   |
|  10.58.1.48 |    RoleService     | 85% |  57%   |
| 10.58.1.129 |    RoleService     |  6% |  32%   |
| 10.58.1.102 |    RoleService     | 90% |  82%   |
| 10.58.1.146 |    RoleService     | 17% |  72%   |
|  10.58.1.22 |    RoleService     | 64% |   5%   |
|  10.58.1.72 |    RoleService     | 74% |   9%   |
|  10.58.1.8  |    RoleService     | 52% |  27%   |
| 10.58.1.101 |    RoleService     | 96% |  73%   |
|  10.58.1.34 |    RoleService     | 61% |  76%   |
|  10.58.1.57 |    AuthService     |  4% |  19%   |
|  10.58.1.61 |    AuthService     | 78% |  81%   |
|  10.58.1.46 |    AuthService     | 31% |   4%   |
|  10.58.1.9  |    AuthService     | 86% |  46%   |
|  10.58.1.81 |    AuthService     | 85% |   0%   |
|  10.58.1.56 |    AuthService     | 33% |  69%   |
|  10.58.1.84 |    AuthService     | 19% |  25%   |
| 10.58.1.145 |    AuthService     | 68% |  90%   |
|  10.58.1.88 |    AuthService     | 28% |  70%   |
|  10.58.1.25 |    AuthService     | 58% |   3%   |
| 10.58.1.109 |    AuthService     | 38% |  68%   |
| 10.58.1.107 |    AuthService     | 57% |  86%   |
| 10.58.1.147 |    AuthService     | 66% |  93%   |
|  10.58.1.35 |    AuthService     |  0% |  51%   |
|  10.58.1.95 |    AuthService     | 89% |  36%   |
|  10.58.1.28 |    AuthService     | 54% |  91%   |
|  10.58.1.89 |    AuthService     | 52% |  44%   |
| 10.58.1.104 |   TicketService    | 56% |  21%   |
|  10.58.1.60 |   TicketService    | 38% |  17%   |
| 10.58.1.135 |   TicketService    | 96% |   6%   |
|  10.58.1.13 |   TicketService    | 27% |  24%   |
| 10.58.1.111 |   TicketService    | 52% |   2%   |
| 10.58.1.113 |   TicketService    | 83% |  53%   |
|  10.58.1.50 |   TicketService    | 57% |  95%   |
|  10.58.1.74 |   TicketService    | 65% |  79%   |
|  10.58.1.83 |   StorageService   | 50% |  40%   |
|  10.58.1.4  |   StorageService   | 92% |  99%   |
|  10.58.1.99 |   StorageService   | 39% |  98%   |
|  10.58.1.39 |   StorageService   | 31% |  15%   |
|  10.58.1.53 |   StorageService   | 82% |  33%   |
| 10.58.1.114 |   StorageService   | 14% |  72%   |
|  10.58.1.43 |   StorageService   | 82% |  87%   |
| 10.58.1.136 |   StorageService   | 74% |  25%   |
|  10.58.1.5  |   StorageService   | 91% |  88%   |
|  10.58.1.1  |   StorageService   | 46% |   8%   |
| 10.58.1.137 |   StorageService   | 40% |  10%   |
|  10.58.1.6  |   StorageService   | 47% |   6%   |
|  10.58.1.82 |   StorageService   |  4% |  23%   |
|  10.58.1.15 |   StorageService   | 74% |  65%   |
|  10.58.1.69 |   StorageService   | 76% |  48%   |
|  10.58.1.73 |   StorageService   | 59% |  10%   |
|  10.58.1.2  |    TimeService     | 28% |  71%   |
|  10.58.1.58 |    TimeService     |  8% |  37%   |
|  10.58.1.38 |    TimeService     | 14% |   1%   |
|  10.58.1.37 |    TimeService     | 60% |  97%   |
|  10.58.1.23 |    TimeService     | 73% |  27%   |
| 10.58.1.110 |    TimeService     | 19% |  36%   |
|  10.58.1.45 |    TimeService     | 59% |  18%   |
|  10.58.1.85 |    TimeService     | 20% |  58%   |
| 10.58.1.139 |    TimeService     | 37% |  34%   |
|  10.58.1.32 |    TimeService     | 21% |  87%   |
|  10.58.1.70 |    UserService     | 71% |   9%   |
| 10.58.1.141 |    UserService     | 48% |   6%   |
| 10.58.1.131 |    UserService     | 31% |   0%   |
|  10.58.1.31 |    UserService     | 68% |  15%   |
| 10.58.1.149 |    UserService     | 54% |  59%   |
| 10.58.1.121 |    UserService     | 26% |  54%   |
| 10.58.1.143 |    UserService     | 35% |  10%   |
|  10.58.1.77 |    UserService     | 20% |   0%   |
|  10.58.1.98 |    UserService     |  8% |  59%   |
|  10.58.1.52 |    UserService     |  5% |  24%   |
+-------------+--------------------+-----+--------+

```

**Design Thoughts**

`CpxMonitor` class takes care of capturing services and hosts information from the CPX Monitoring service. All printing/output features are handled by it.

`ServiceInfo` class holds information on a service and hosts that belong to it.

`HostInfo` class holds information on a single host.

The tool uses `prettytable` python package to pretty print the hosts and services information in a table.

Improvements that can be done -
- Better handle errors in fetching data from CPX Monitoring service
- Service tracking feature clears the screen right now which might not be very user-friendly
and hence look to improve that by updating it to just re-write the tables in the same space in
the terminal which I believe can be a tedious job.
- Add ability to sort and filter tabular services data.
- Add test to validate that the `ServiceInfo` objects are refreshed in the `CpxMonitor` class for tracking feature.
- Add type hints for a better developer experience.

**How to Run tests**

```
Inside the repository -

source testenv/bin/activate

pytest tests/* -v -s

```