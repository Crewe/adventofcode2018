import io

class Claim:
    def __init__(self, id=-1, x=0, y=0, width=0, height=0):
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    def validateClaim(self):
        if (self.width == 0 or self.height == 0 or self.id < 0):
            raise Exception("Invalid claim")

    def x():
        return self.x

    def y():
        return self.y

    def width():
        return self.width
    
    def height():
        return self.height

    def id():
        return self.id

class Fabric:
    def __init__(self):
        self.layout = [[None]]
        self.claims = set()
        self.solitary_claims = set()
        self.x = 0
        self.y = 0
    
    def increaseX(self, x):
        self.x += x

    def increaseY(self, y):
        self.y += y

    def increaseXY(self, x, y):
        if x > 0: self.increaseX(x)
        if y > 0: self.increaseY(y)

    def addClaim(self, claim):
        # If the claim extends beyond the fabric
        # grow the fabric and add the claim
        if ((claim.x + claim.width) > self.x) or ((claim.y + claim.height) > self.y):
            delta_x = (claim.x + claim.width) - self.x
            delta_y = (claim.y + claim.height) - self.y
            self.resizeFabric(delta_x, delta_y)

        if (self.layout[claim.y][claim.x] == None):
            self.layout[claim.y][claim.x] = [claim]
        else:
            self.layout[claim.y][claim.x].append(claim)

    def resizeFabric(self, delta_x, delta_y):
        old_size = [self.x, self.y]
        self.increaseXY(delta_x, delta_y)
        new_fab_layout = [[None] * self.x for i in range(self.y)]

        for y_ in range(old_size[1]):
            for x_ in range(old_size[0]):
                new_fab_layout[y_][x_] = self.layout[y_][x_]
        self.layout = new_fab_layout

    def getClaims(self, x, y):
        return self.layout[y][x]
    
    def layout():
        return self.layout

    def totalClaims():
        return self.total_claims

    def solitaryClaims():
        return self.solitary_claims

def getInput(filename):
    value_array = []
    with open(filename) as f:
        for line in f:
            value_array.append(line.replace('\n',''))
    return value_array

def processClaims(claims, fabric=Fabric()):
    for claim in claims:
        new_claim = Claim()
        tmp = claim.split(' ')
        new_claim.id = int(tmp[0].replace('#',''))
        new_claim.x, new_claim.y = [int(val) for val in tmp[2].replace(':', '').split(',')]
        new_claim.width, new_claim.height = [int(val) for val in tmp[3].split('x')]
        new_claim.validateClaim()
        fabric.addClaim(new_claim)
    return fabric

def plotClaim(claim_map, claim_list):
    for claim in claim_list:
        id = claim.id
        for y_ in range(claim.y, claim.y + claim.height):
            for x_ in range(claim.x, claim.x + claim.width):
                if claim_map[y_][x_] == None:
                    claim_map[y_][x_] = [id]
                else:
                    claim_map[y_][x_].append(id)

    return claim_map

def findClaimOverlap(fabric):
    overlaps = 0
    width = fabric.x
    height = fabric.y
    overlays = [[None] * width for i in range(height)]

    for y_ in range(height):
        for x_ in range(width):
            claims = fabric.getClaims(x_, y_)
            if claims != None:
                overlays = plotClaim(overlays, claims)

    for y_ in range(height):
        for x_ in range(width):
            if overlays[y_][x_] != None and len(overlays[y_][x_]) > 1:
                overlaps += 1

    return overlaps, overlays

def findIsolatedClaims(claim_map, width, height):
    shared = set()
    ids = set()
    for y_ in range(height):
        for x_ in range(width):
            if claim_map[y_][x_] != None:
                tmp = set(claim_map[y_][x_])
                ids = ids.union(tmp)
                if len(tmp) >= 2:
                    shared = shared.union(tmp)

    return ids.difference(shared)

def writeClaimsToFile(filename, claim_map):
    f = open(filename, 'w')
    for y_ in range(len(claim_map)):
        f.write(str(claim_map[y_]) + "\n")

magic_fabric = Fabric()
claims = getInput("input3.txt")
magic_fabric = processClaims(claims, magic_fabric)
overlayed, claim_map = findClaimOverlap(magic_fabric)
iso_ids = findIsolatedClaims(claim_map, len(claim_map[0]), len(claim_map))
#writeClaimsToFile("claims.map", claim_map)
print("The magic fabric is {}units x {}units.".format(magic_fabric.x, magic_fabric.y))
print("There are {}units^2 of overlap.".format(overlayed))
print("ID(s) which have no overlap: {}.".format(iso_ids))
