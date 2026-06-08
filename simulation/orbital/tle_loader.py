from typing import List, Dict


class TLELoader:

    def load_tle_file(
        self,
        filepath: str
    ) -> List[Dict[str, str]]:

        satellites = []

        with open(filepath, "r") as f:

            lines = [
                line.strip()
                for line in f.readlines()
                if line.strip()
            ]

        if len(lines) % 3 != 0:
            raise ValueError(
                "Invalid TLE file. Expected groups of 3 lines."
            )

        for i in range(0, len(lines), 3):

            satellites.append({
                "name": lines[i],
                "line1": lines[i + 1],
                "line2": lines[i + 2]
            })

        return satellites