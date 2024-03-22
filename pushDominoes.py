 def pushDominoes(self, dominoes):
        n = len(dominoes)
        forces = [0] * n

        # Left to Right pass
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # Right to Left pass
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # Construct the final state string
        result = ''
        for force in forces:
            if force == 0:
                result += '.'
            elif force > 0:
                result += 'R'
            else:
                result += 'L'

        return result
