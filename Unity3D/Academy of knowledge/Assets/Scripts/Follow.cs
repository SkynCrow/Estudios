using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Follow : MonoBehaviour
{
    public Transform objetive;
    public Vector3 offset;
    
    void Update()
    {
        transform.position = objetive.transform.position + offset;
    }
}
