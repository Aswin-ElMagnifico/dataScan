
class Firms_import:
    def __init__(self, fname, iname, iref, date):
        self.fname = fname
        self.iname = iname
        self.iref = iref
        self.date = date


class FEIContainer:
    def __init__(self, fei_id, insp, inspc, compc, reca, refu, warn):
        self.fei_id = fei_id
        self.insp = insp
        self.inspc = inspc
        self.compc = compc
        self.reca = reca
        self.refu = refu
        self.warn = warn

    def display(self):
        print("Firm no: " + self.fei_id)
        print("Inspection details")
        try:
            for stuff in self.insp:
                print("inspection id: " + stuff[0])
                print("inspection end date: " + stuff[1])
                print("project area: " + stuff[2])
                print("product type: " + stuff[3])
                print("classification: " + stuff[4])
        except:
            pass

        print("Inspection Citations details")
        try:
            for stuff in self.inspc:
                print("inspection id: " + stuff[0])
                print("inspection end date: " + stuff[1])
                print("program area: " + stuff[2])
                print("pact/cfr number: " + stuff[3])
                print("short desc: " + stuff[4])
                print("long desc: " + stuff[5])
        except:
            pass

        print("Compliance Details")
        try:
            for stuff in self.compc:
                print("product type: " + stuff[0])
                print("case id" + stuff[1])
                print("action taken date: " + stuff[2])
                print("action type: " + stuff[3])
        except:
            pass

        print("Recall Details")
        for stuff in self.reca:
            print("classification: " + stuff[1])
            print("product type: " + stuff[2])
            print("status: " + stuff[3])
            print("distribution pattern: " + stuff[4])
            print("firm name: " + stuff[5])
            print("center classification data: " + stuff[6])


        print("Import Refusals")
        for stuff in self.refu:
            print("product code: " + stuff[0])
            print("refused date: " + stuff[1])
            print("refusal charge: " + stuff[2])

        print("Warning letters")
        try:
            print("subject: " + self.warn[0])
            print("date: " + self.warn[1])
            print("link: " + self.warn[2])
        except:
            pass
