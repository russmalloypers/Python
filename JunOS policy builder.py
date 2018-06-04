#test1
# coding: utf-8

# In[1]:


#policy_id - determines what the first policy number should be in output
policy_id = "43"

#True if insert policy before default is required, False if otherwise
insert = False

customer_alias = "russ"
destination_zone = "vpn-zone"
vpn_name = "slc-vpn"


source_subnets = ["40","20","30"]
dest_subnets = ["alpha", "beta", "charlie"]

#policy creation
for i in range(len(source_subnets)):
    for y in range(len(dest_subnets)):
        ### Outbound start
        #source-address
        print("set security policies from-zone " + customer_alias + " to-zone " + destination_zone + " policy " + vpn_name + "-ob-" + policy_id + " match source-address " + source_subnets[i])
        
        #destination-address
        print("set security policies from-zone " + customer_alias + " to-zone " + destination_zone + " policy " + vpn_name + "-ob-" + policy_id + " match destination-address " + dest_subnets[y])
        
        #application any
        print("set security policies from-zone " + customer_alias + " to-zone " + destination_zone + " policy " + vpn_name + "-ob-" + policy_id + " match application any")
        
        #permit per vpn
        print("set security policies from-zone " + customer_alias + " to-zone " + destination_zone + " policy " + vpn_name + "-ob-" + policy_id + " then permit tunnel ipsec-vpn " + vpn_name)
        
        #pair-policy
        print("set security policies from-zone " + customer_alias + " to-zone " + destination_zone + " policy " + vpn_name + "-ob-" + policy_id + " then permit tunnel pair-policy " + vpn_name + "-ib-" + policy_id)
        ### Outbound end
        
        #insert if insert=True (required to be above default deny policy if one exists)
        if (insert):
            print("insert security policies from-zone " + customer_alias + " to-zone " + destination_zone + " policy " + vpn_name + "-ob-" + policy_id + " before policy " + customer_alias + "_vpn-zone_default")
        
        ### Inbound start
        #source-address
        print("set security policies from-zone " + destination_zone + " to-zone " + customer_alias + " policy " + vpn_name + "-ib-" + policy_id + " match source-address " + dest_subnets[y])
        
        #destination-address
        print("set security policies from-zone " + destination_zone + " to-zone " + customer_alias + " policy " + vpn_name + "-ib-" + policy_id + " match destination-address " + source_subnets[i])

        #application any
        print("set security policies from-zone " + destination_zone + " to-zone " + customer_alias + " policy " + vpn_name + "-ib-" + policy_id + " match application any")

        #permit per vpn
        print("set security policies from-zone " + destination_zone + " to-zone " + customer_alias + " policy " + vpn_name + "-ib-" + policy_id + " then permit tunnel ipsec-vpn " + vpn_name)

        #pair-policy
        print("set security policies from-zone " + destination_zone + " to-zone " + customer_alias + " policy " + vpn_name + "-ib-" + policy_id + " then permit tunnel pair-policy " + vpn_name + "-ob" + policy_id)
        ### Inbound end
        
        #insert if insert=True (required to be above default deny policy if one exists)
        if (insert):
            print("insert security policies from-zone " + destination_zone + " to-zone " + customer_alias + " policy " + vpn_name + "-ib-" + policy_id + " before policy vpn-zone_" + customer_alias + "_default")
        
        #increment policy_id. Convert to int, add 1, convert back to string
        policy_id = int(policy_id)
        policy_id += 1
        policy_id = str(policy_id)
        
        #print blank line
        print("")

#create address book entries
print ("# Address Book Entries")
for i in range(len(dest_subnets)):
    print("set security address-book global address " + dest_subnets[i] + " " + dest_subnets[i])
        

